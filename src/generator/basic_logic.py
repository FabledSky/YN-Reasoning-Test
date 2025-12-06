"""Basic propositional logic items."""

from __future__ import annotations

from .models import GeneratedItem, build_item


FAMILY = "basic_logic"


def _truth_word(value: bool) -> str:
    """Return a short string describing the truth value."""

    return "true" if value else "false"


def conjunction_truth(p: bool, q: bool) -> GeneratedItem:
    """Return whether two claims are simultaneously true."""

    statement = (
        f"Claim A is {_truth_word(p)} and claim B is {_truth_word(q)}, so both together are true."
    )
    return build_item(text=statement, answer=p and q, family=FAMILY)


def negation_flip(value: bool) -> GeneratedItem:
    """Return whether the negation of a claim is true."""

    statement = f"The negation of a {_truth_word(value)} claim is {_truth_word(not value)}."
    return build_item(text=statement, answer=not value, family=FAMILY)


def conditional_truth(p: bool, q: bool) -> GeneratedItem:
    """Return the truth of a simple conditional based on two claims."""

    statement = (
        f"With claim A {_truth_word(p)} and claim B {_truth_word(q)}, the conditional 'if A then B' is true."
    )
    answer = (not p) or q
    return build_item(text=statement, answer=answer, family=FAMILY)


__all__ = ["conjunction_truth", "negation_flip", "conditional_truth", "FAMILY"]
