# API Example: Requesting Items and Reading Answers

This example shows how to request generated True/False items from the Python
modules and how to read boolean answers from the returned dataclass objects.

```python
from src.generator import arithmetic, number_properties

# Request a new item asking about an addition fact.
item = arithmetic.addition_equals(4, 7, proposed_sum=11)
print(item.text)    # Adding 4 and 7 gives 11.
print(item.answer)  # True
print(item.family)  # arithmetic

# Another item from a different family.
prime_item = number_properties.is_prime(15)
print(prime_item.text)    # The number 15 is a prime number.
print(prime_item.answer)  # False
```

Each function returns a dataclass with fields that mirror the JSON schema used
in `data/items_raw.json`:

- `id`: Unique string identifier.
- `text`: Single-sentence, ESL-friendly statement.
- `answer`: Boolean indicating whether the statement is true.
- `family`: Item family such as `"arithmetic"` or `"number_properties"`.
- `difficulty`: Optional numeric difficulty (often `None` for new items).
- `status`, `source`, `notes`: Metadata maintained by the generators.

When evaluating user submissions, compare the user's boolean response to
`item.answer`. The `src/scoring/scoring_model.py` placeholder provides a simple
`placeholder_scorer` function you can swap for IRT-based scoring later.
