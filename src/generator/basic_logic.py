"""Generators for foundational logical connectives."""

from __future__ import annotations

from .models import GeneratedItem, build_item


FAMILY = "basic_logic"


def conjunction_truth(p: bool, q: bool) -> GeneratedItem:
    """Return an item about the truth of a conjunction."""

    statement = "If both statements are true, then their conjunction is true."
    return build_item(text=statement, answer=p and q, family=FAMILY)


def negation_flip(value: bool) -> GeneratedItem:
    """Return an item noting that a negation inverts truth."""

    statement = "If a statement is true, its negation is false."
    return build_item(text=statement, answer=value is True, family=FAMILY)


def conditional_truth(p: bool, q: bool) -> GeneratedItem:
    """Return an item about a simple conditional."""

    statement = "If the first claim is true and the second is false, the conditional is false."
    answer = not (p and not q)
    return build_item(text=statement, answer=answer, family=FAMILY)


__all__ = ["conjunction_truth", "negation_flip", "conditional_truth", "FAMILY"]
