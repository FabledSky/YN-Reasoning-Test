"""Generators for simple points and scoring logic items."""

from __future__ import annotations

from .models import GeneratedItem, build_item


FAMILY = "points_scoring"


def match_points(goals: int, assists: int, points_for_goal: int = 2, points_for_assist: int = 1) -> GeneratedItem:
    """Check the total points earned from goals and assists."""

    total_points = goals * points_for_goal + assists * points_for_assist
    statement = f"With {goals} goals and {assists} assists, the player earned {total_points} points."
    return build_item(text=statement, answer=True, family=FAMILY)


def bonus_threshold(score: int, threshold: int) -> GeneratedItem:
    """Check whether a score meets or exceeds a bonus threshold."""

    statement = f"A score of {score} reaches the bonus threshold of {threshold}."
    return build_item(text=statement, answer=score >= threshold, family=FAMILY)


__all__ = ["match_points", "bonus_threshold", "FAMILY"]
