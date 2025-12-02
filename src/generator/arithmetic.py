"""Generators for arithmetic True/False items."""

from __future__ import annotations

from .models import GeneratedItem, build_item


FAMILY = "arithmetic"


def addition_equals(a: int, b: int, proposed_sum: int) -> GeneratedItem:
    """Return an item asking if ``a + b`` equals ``proposed_sum``.

    The statement is intentionally short and uses digits to support ESL readers.
    """

    statement = f"Adding {a} and {b} gives {proposed_sum}."
    return build_item(text=statement, answer=a + b == proposed_sum, family=FAMILY)


def multiplication_comparison(a: int, b: int, threshold: int) -> GeneratedItem:
    """Return an item comparing a product to a threshold."""

    product = a * b
    statement = f"The product of {a} and {b} is at least {threshold}."
    return build_item(text=statement, answer=product >= threshold, family=FAMILY)


def division_whole(a: int, b: int) -> GeneratedItem:
    """Return an item checking whether ``a`` divides evenly by ``b``."""

    statement = f"{a} divided by {b} is a whole number."
    answer = b != 0 and a % b == 0
    return build_item(text=statement, answer=answer, family=FAMILY)


__all__ = [
    "addition_equals",
    "multiplication_comparison",
    "division_whole",
    "FAMILY",
]
