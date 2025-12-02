"""Generators for ordering and ranking statements."""

from __future__ import annotations

from .models import GeneratedItem, build_item


FAMILY = "ordering"


def ascending_triple(a: int, b: int, c: int) -> GeneratedItem:
    """Check whether three numbers are in strict ascending order."""

    statement = f"The numbers {a}, {b}, {c} are in ascending order."
    return build_item(text=statement, answer=a < b < c, family=FAMILY)


def position_in_line(position: int, total: int) -> GeneratedItem:
    """Check whether a position is valid within a line of a given size."""

    statement = f"Position {position} is within a line of {total} people."
    return build_item(text=statement, answer=1 <= position <= total, family=FAMILY)


__all__ = ["ascending_triple", "position_in_line", "FAMILY"]
