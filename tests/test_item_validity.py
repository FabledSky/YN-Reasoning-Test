import json
import re
from pathlib import Path
from typing import Iterable, Optional

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

ALLOWED_FAMILIES = {
    "arithmetic",
    "number_properties",
    "patterns",
    "transitivity",
    "sets_logic",
    "ordering",
    "points_scoring",
    "basic_logic",
}

ALLOWED_STATUS = {"draft", "approved", "retired"}


def load_items(filename: str) -> list[dict]:
    with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


def assert_schema(item: dict, *, require_version: bool = False) -> None:
    required_keys = {"id", "text", "answer", "family", "difficulty", "status", "source", "notes"}
    assert required_keys.issubset(item.keys())

    assert isinstance(item["id"], str) and item["id"].strip()
    assert isinstance(item["text"], str) and item["text"].strip()
    assert isinstance(item["answer"], bool)
    assert item["family"] in ALLOWED_FAMILIES
    assert item["status"] in ALLOWED_STATUS

    difficulty = item["difficulty"]
    assert difficulty is None or isinstance(difficulty, (int, float))

    assert isinstance(item["source"], str)
    assert isinstance(item["notes"], str)

    if "tags" in item:
        assert isinstance(item["tags"], list)
        assert all(isinstance(tag, str) and tag.strip() for tag in item["tags"])

    if require_version:
        assert "version" in item
    if "version" in item:
        assert isinstance(item["version"], int) and item["version"] > 0


def count_sentence_endings(text: str) -> int:
    return sum(text.count(punct) for punct in ".?!")


def is_single_sentence(text: str) -> bool:
    return count_sentence_endings(text) == 1 and text.rstrip().endswith(('.', '?', '!'))


def is_esl_friendly_length(text: str, *, max_words: int = 25) -> bool:
    return len(text.split()) <= max_words


ALLOWED_CHARS_PATTERN = re.compile(r"^[A-Za-z0-9 ,.;:'\"+\-!?=()]*$")


def has_allowed_characters(text: str) -> bool:
    return text.isascii() and bool(ALLOWED_CHARS_PATTERN.match(text))


def recompute_arithmetic_answer(text: str) -> Optional[bool]:
    match = re.match(r"^(?P<a>-?\d+) \+ (?P<b>-?\d+) equals (?P<c>-?\d+)\.?", text, flags=re.IGNORECASE)
    if not match:
        return None
    a = int(match.group("a"))
    b = int(match.group("b"))
    c = int(match.group("c"))
    return a + b == c


def recompute_pattern_truth(text: str) -> Optional[bool]:
    sequence_match = re.search(r"sequence\s+([0-9 ,]+)", text, flags=re.IGNORECASE)
    if not sequence_match:
        return None

    numbers = [int(part.strip()) for part in sequence_match.group(1).split(",") if part.strip()]
    if len(numbers) < 2:
        return None

    if re.search(r"doubles each step", text, flags=re.IGNORECASE):
        return all(numbers[idx] == numbers[idx - 1] * 2 for idx in range(1, len(numbers)))

    return None


def gather_items(filenames: Iterable[str]) -> list[dict]:
    collected: list[dict] = []
    for filename in filenames:
        collected.extend(load_items(filename))
    return collected


def test_items_schema_and_values():
    raw_items = load_items("items_raw.json")
    clean_items = load_items("items_clean.json")

    for item in raw_items:
        assert_schema(item)

    for item in clean_items:
        assert_schema(item, require_version=True)
        assert item["status"] != "draft"
        assert item["difficulty"] is None or item["difficulty"] >= 0


def test_single_sentence_and_length_and_characters():
    for item in gather_items(["items_raw.json", "items_clean.json"]):
        text = item["text"].strip()
        assert is_single_sentence(text), f"Item {item['id']} is not a single sentence"
        assert is_esl_friendly_length(text), f"Item {item['id']} exceeds ESL-friendly length"
        assert has_allowed_characters(text), f"Item {item['id']} contains unsupported characters"


def test_boolean_answers():
    for item in gather_items(["items_raw.json", "items_clean.json"]):
        assert isinstance(item["answer"], bool)


def test_arithmetic_items_are_consistent():
    recognized = 0
    for item in gather_items(["items_raw.json", "items_clean.json"]):
        if item["family"] != "arithmetic":
            continue
        recomputed = recompute_arithmetic_answer(item["text"])
        if recomputed is None:
            continue
        recognized += 1
        assert recomputed == item["answer"], f"Arithmetic mismatch for {item['id']}"

    assert recognized > 0, "No arithmetic templates were recognized for consistency checks"


def test_pattern_items_are_consistent():
    recognized = 0
    for item in gather_items(["items_raw.json", "items_clean.json"]):
        if item["family"] != "patterns":
            continue
        recomputed = recompute_pattern_truth(item["text"])
        if recomputed is None:
            continue
        recognized += 1
        assert recomputed == item["answer"], f"Pattern mismatch for {item['id']}"

    assert recognized > 0, "No pattern templates were recognized for consistency checks"
