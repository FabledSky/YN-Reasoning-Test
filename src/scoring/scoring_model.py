"""Lightweight scoring primitives for True/False responses.

This module sketches how item responses may be scored. Implementations should
stay pure and independent from storage or transport concerns. The current
placeholder keeps the API visible without enforcing a concrete dependency.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class ResponseScorer(Protocol):
    """Protocol describing the callable signature for scoring a response."""

    def __call__(self, *, correct: bool, response: bool) -> float:  # pragma: no cover - placeholder
        """Return a numeric score, such as log-likelihood or partial credit."""


@dataclass
class IRTParameters:
    """Minimal container for IRT-style parameters.

    Fields mirror the common three-parameter logistic model but can be extended
    later. This dataclass exists to clarify the data shape expected by a future
    scorer implementation.
    """

    difficulty: float
    discrimination: float
    guessing: float = 0.0


def placeholder_scorer(*, correct: bool, response: bool) -> float:
    """Return ``1.0`` for correct matches, else ``0.0``.

    Replace this with an IRT-based likelihood or a rule-based rubric once
    response data is available.
    """

    return 1.0 if correct is response else 0.0
