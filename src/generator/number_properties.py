"""Generators for number property items such as evenness and primes."""

from __future__ import annotations

from math import isqrt

from .models import GeneratedItem, build_item


FAMILY = "number_properties"


def is_even(number: int) -> GeneratedItem:
    """Return an item asking if the number is even."""

    statement = f"The number {number} is even."
    return build_item(text=statement, answer=number % 2 == 0, family=FAMILY)


def is_prime(number: int) -> GeneratedItem:
    """Return an item asking if the number is prime."""

    if number < 2:
        answer = False
    else:
        answer = all(number % divisor != 0 for divisor in range(2, isqrt(number) + 1))
    statement = f"The number {number} is a prime number."
    return build_item(text=statement, answer=answer, family=FAMILY)


def greater_than(a: int, b: int) -> GeneratedItem:
    """Return an item comparing two values."""

    statement = f"{a} is greater than {b}."
    return build_item(text=statement, answer=a > b, family=FAMILY)


__all__ = [
    "is_even",
    "is_prime",
    "greater_than",
    "FAMILY",
]
