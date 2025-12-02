"""Generators for ordering and relational transitivity items."""

from __future__ import annotations

from .models import GeneratedItem, build_item


FAMILY = "transitivity"


def greater_chain(a: int, b: int, c: int) -> GeneratedItem:
    """Check if a transitive greater-than relation holds."""

    statement = f"If {a} is greater than {b} and {b} is greater than {c}, then {a} is greater than {c}."
    return build_item(text=statement, answer=a > b > c, family=FAMILY)


def height_comparison(a_taller_than_b: bool, b_taller_than_c: bool) -> GeneratedItem:
    """State whether A is taller than C given two comparisons."""

    statement = "If Alex is taller than Blair and Blair is taller than Casey, then Alex is taller than Casey."
    answer = a_taller_than_b and b_taller_than_c
    return build_item(text=statement, answer=answer, family=FAMILY)


__all__ = ["greater_chain", "height_comparison", "FAMILY"]
