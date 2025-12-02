"""Shared dataclasses and helpers for generated True/False items."""

from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4


@dataclass(slots=True)
class GeneratedItem:
    """Representation of a single True/False reasoning item.

    Attributes mirror the JSON schema stored in ``data/items_raw.json``. The
    ``text`` field must always be a single, ESL-friendly sentence.
    """

    id: str
    text: str
    answer: bool
    family: str
    difficulty: Optional[float]
    status: str = "draft"
    source: str = "auto_generated"
    notes: str = ""


def build_item(
    *,
    text: str,
    answer: bool,
    family: str,
    difficulty: Optional[float] = None,
    status: str = "draft",
    source: str = "auto_generated",
    notes: str = "",
) -> GeneratedItem:
    """Create a :class:`GeneratedItem` with a fresh UUID.

    The helper keeps all generator functions consistent with the JSON schema and
    centralizes defaults for status, source, and notes.
    """

    return GeneratedItem(
        id=str(uuid4()),
        text=text,
        answer=answer,
        family=family,
        difficulty=difficulty,
        status=status,
        source=source,
        notes=notes,
    )
