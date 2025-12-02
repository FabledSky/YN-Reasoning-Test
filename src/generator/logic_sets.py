"""Generators for basic set membership and relationship items."""

from __future__ import annotations

from .models import GeneratedItem, build_item


FAMILY = "sets_logic"


def element_membership(element: str, group: set[str]) -> GeneratedItem:
    """State whether an element is in the given group."""

    group_display = ", ".join(sorted(group)) if group else "(empty set)"
    statement = f"The element '{element}' is in the set {{{group_display}}}."
    return build_item(text=statement, answer=element in group, family=FAMILY)


def subset_relation(subset: set[str], superset: set[str]) -> GeneratedItem:
    """Check whether one set is a subset of another."""

    subset_display = ", ".join(sorted(subset)) if subset else "(empty)"
    superset_display = ", ".join(sorted(superset)) if superset else "(empty)"
    statement = f"Set {{{subset_display}}} is a subset of set {{{superset_display}}}."
    return build_item(text=statement, answer=subset.issubset(superset), family=FAMILY)


__all__ = ["element_membership", "subset_relation", "FAMILY"]
