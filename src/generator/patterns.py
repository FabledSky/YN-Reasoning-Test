"""Generators for numeric pattern continuation items."""

from __future__ import annotations

from .models import GeneratedItem, build_item


FAMILY = "patterns"


def next_in_arithmetic_sequence(start: int, step: int, length: int, proposal: int) -> GeneratedItem:
    """Check whether the proposal is the next number in an arithmetic sequence."""

    expected_next = start + step * length
    sequence_preview = ", ".join(str(start + step * i) for i in range(length))
    statement = f"In the pattern {sequence_preview}, the next number is {proposal}."
    return build_item(text=statement, answer=proposal == expected_next, family=FAMILY)


def repeating_block(block: str, position: int, proposal: str) -> GeneratedItem:
    """Check whether the proposed symbol matches a repeating pattern."""

    if not block:
        raise ValueError("block must not be empty")

    expected_symbol = block[(position - 1) % len(block)]
    statement = f"In the repeating pattern '{block}', position {position} is '{proposal}'."
    return build_item(text=statement, answer=proposal == expected_symbol, family=FAMILY)


__all__ = ["next_in_arithmetic_sequence", "repeating_block", "FAMILY"]
