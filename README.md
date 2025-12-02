# Fabled Sky – Yes/No Reasoning Test
v. 1.0.2

A culture-reduced, **yes/no (true/false)** reasoning test designed to estimate general intelligence using **simple English** and **abstract word problems only** (no images, no diagrams).

The long-term goal is to build a large item bank and scoring model that **correlates strongly with standard IQ measures**, while:
- Avoiding culture-specific knowledge and trivia  
- Keeping language **ESL-friendly**  
- Using only **single-sentence true/false statements**

---

## Table of Contents

1. [Quickstart (Setup & Usage)](#quickstart-setup--usage)
   - [Environment Setup](#environment-setup)
   - [Generate Sample Items](#generate-sample-items)
   - [Run Checks](#run-checks)
2. [Project Goals](#project-goals)
3. [High-Level Design](#high-level-design)
4. [Test Format](#test-format)
5. [Design Principles](#design-principles)
6. [Language Guidelines (ESL-Friendly)](#language-guidelines-esl-friendly)
7. [Item Families (Question Types)](#item-families-question-types)
   - [Arithmetic Comparisons](#1-arithmetic-comparisons)
   - [Number Properties](#2-number-properties)
   - [Lists and Patterns](#3-lists-and-patterns)
   - [Transitive Comparisons](#4-transitive-comparisons)
   - [Set / Category Logic](#5-set--category-logic)
   - [Ordering / Spatial Reasoning](#6-ordering--spatial-reasoning)
   - [Points and Scoring Problems](#7-points-and-scoring-problems)
   - [Basic Logical Rules (If/Then/All/Some)](#8-basic-logical-rules-ifthenallsome)
8. [Difficulty and Item Bank Expansion](#difficulty-and-item-bank-expansion)
9. [Psychometrics and Validation](#psychometrics-and-validation)
10. [Repository Structure (Proposed)](#repository-structure-proposed)
11. [Contributing](#contributing)

---

## Quickstart (Setup & Usage)

The repository ships with a minimal, standard-library-only codebase so you can start generating or validating True/False items immediately. Follow the steps below to try the generators, persist items to JSON, and run the automated checks.

### Environment Setup

1. Install **Python 3.10+**.
2. Clone the repository and create an isolated environment:

   ```bash
   git clone https://github.com/your-org/YN-Reasoning-Test.git
   cd YN-Reasoning-Test
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\\Scripts\\activate
   ```

3. Install **pytest** if you plan to run the tests (the core generators use only the standard library):

   ```bash
   pip install pytest
   ```

### Generate Sample Items

1. Use the generator modules in `src/generator/` to create True/False items. This snippet produces three arithmetic items and writes them to `data/items_raw.json` with two-space indentation:

   ```bash
   python - <<'PY'
   import json
   from dataclasses import asdict
   from pathlib import Path

   from src.generator import arithmetic

   items = [
       arithmetic.addition_equals(3, 4, 7),
       arithmetic.multiplication_comparison(2, 5, 9),
       arithmetic.division_whole(12, 3),
   ]

   data_path = Path("data/items_raw.json")
   if data_path.exists():
       current = json.loads(data_path.read_text(encoding="utf-8"))
   else:
       current = []

   current.extend(asdict(item) for item in items)
   data_path.write_text(json.dumps(current, indent=2), encoding="utf-8")
   print(f"Saved {len(items)} items to {data_path}")
   PY
   ```

2. To load approved items for delivery, read `data/items_clean.json` (same schema as above) and render one sentence at a time in your UI. Each record includes:

   - `id`: string UUID
   - `text`: single-sentence True/False prompt
   - `answer`: boolean
   - `family`: one of the supported families listed below
   - Optional metadata: `difficulty`, `status`, `source`, `notes`

### Run Checks

Execute the test suite to validate schema rules, single-sentence enforcement, and family names:

```bash
pytest
```

Tests live in `tests/` and cover JSON validation plus ESL-friendly constraints.

---

## Project Goals

This project aims to create a **general reasoning test** that:

- Uses **100 items** (per test form)  
- Each item is a **single sentence**  
- Each item is answered **Yes/No** or **True/False**  
- Uses **simple, professional English**, suitable for **ESL** (English as a Second Language) users  
- Avoids:
  - Culture-specific content  
  - School-specific curriculum (e.g., history, literature, local references)  
  - Complex language and idioms  

The test is intended to be:

- **Language-simple** but **conceptually challenging**  
- **Culturally light**, so that a person in Cambodia, South Africa, or the U.S. can reasonably attempt it  
- A foundation for building a **large item bank** for adaptive testing and research on g (general intelligence)

---

## High-Level Design

- **Item format:** one sentence, answered True/False (or Yes/No)  
- **No visual content:** no images, diagrams, graphs, or tables inside items  
- **Content domains:**  
  - Logical relations and transitivity  
  - Basic arithmetic and quantitative comparison  
  - Patterns and sequences  
  - Ordering and spatial reasoning (in words)  
  - Simple set/category logic  
  - Simple scoring/points problems  
  - Basic if/then and quantifier logic (all, some, none)

- **Scoring:**  
  - Each item is marked correct/incorrect.  
  - Because T/F has 50% guessing probability, we rely on:
    - A relatively **large number of items** (100+)  
    - A mix of **difficulty levels**  
    - **Psychometric analysis** (item response theory, correlations with external IQ tests) to calibrate scores

---

## Test Format

- **Number of items:** 100 (per standard form)  
- **Response format:**  
  - Boolean: `True` or `False` (or `Yes` / `No`, but internally treated as a boolean)  
- **Item display:**  
  - Exactly **one sentence** per item  
  - No extra paragraphs or sub-bullets in the test UI  
- **Time limits:**  
  - TBD; can be configured per deployment (e.g., ~30–45 minutes for 100 items)

---

## Design Principles

1. **Measure reasoning, not schooling.**  
   - Avoid vocabulary tests, spelling, reading comprehension, and factual knowledge.  
   - Focus on **relations**, **patterns**, and **logical consistency**.

2. **Culture-reduced, not culture-free.**  
   - We allow basic concepts like **numbers, comparison words, simple names**, etc.  
   - We avoid local customs, pop culture, and region-specific references.

3. **ESL-friendly language.**  
   - Simple grammar and vocabulary (roughly A2–B1 CEFR).  
   - No idioms, slang, or complex academic connectives (“therefore,” “consequently,” etc.).  
   - Clear, consistent patterns across items.

4. **Abstract content.**  
   - Use letters (A, B, C) or simple pseudowords (Zors, Blins) for categories.  
   - Use basic shapes (star, circle, square) and points for scoring items.  
   - Use digits for numbers (5, 12, 30) rather than spelled-out words.

5. **Single-sentence constraint.**  
   - Every question is a **single sentence**, even if it contains an embedded rule:
     - ✅ “If a star is worth 3 points and a circle is worth 2 points, then two stars and one circle are worth 8 points.”  
     - ❌ Multi-sentence instructions for one item.

6. **No trickery.**  
   - Avoid double negatives or unclear wording.  
   - Difficulty should come from the **reasoning**, not from confusing language.

---

## Language Guidelines (ESL-Friendly)

To keep items understandable for basic English speakers, we define a **style guide**:

### Grammar

- Prefer **simple present tense**:  
  - “A is taller than B.”  
  - “In this list, each number is 2 more than the one before it.”

- Use a small set of recurring structures:
  - `In this list: ..., each number is ... more/less than the number before it.`  
  - `If A is ... than B and B is ... than C, then ...`  
  - `If X is worth ... points and Y is worth ... points, then ...`  
  - `If all X are Y and all Y are Z, then ...`

### Vocabulary

Allowed core words (non-exhaustive, but representative):

- **Math words:**  
  - `plus`, `minus`, `times`, `more than`, `less than`, `equal to`, `half`, `double`, `one third`, `one fourth`
- **Comparison:**  
  - `taller`, `shorter`, `older`, `younger`, `heavier`, `lighter`, `left`, `right`, `between`, `before`, `after`
- **Logic:**  
  - `if`, `then`, `and`, `or`, `all`, `some`, `no`, `always`, `never`
- **Objects:**  
  - `number`, `list`, `row`, `seat`, `box`, `house`, `group`, `points`, `shape`, `star`, `circle`, `square`, `triangle`

Recommend avoiding:

- Rare or advanced words: `divisible`, `remainder`, `consequently`, `inconsistent`, `contradiction`  
- Idioms: `rule of thumb`, `on the other hand`, `by and large`, etc.  
- Nested clauses with multiple “if/then/and/or” chains in one sentence.

If advanced words are needed (e.g., *divisible*), define them once in **instructions** and keep the item sentences themselves as simple as possible.

---

## Item Families (Question Types)

This section describes the main **templates** we use to generate questions, with example items.

All example items are intended to be **one sentence** and **True/False**.

---

### 1. Arithmetic Comparisons

**Concept:** Compare simple expressions with +, −, × and relationships like “greater than,” “less than,” “equal to,” “half,” and “double.”

**Template examples:**

- `X plus Y is greater than A plus B.`  
- `X times Y is equal to A times B.`  
- `Half of N is M.`  
- `Double of N is M.`  

**Example items:**

1. **“7 plus 5 is greater than 3 plus 8.”**  
   → 12 > 11 → **True**

2. **“9 times 2 is equal to 3 times 5.”**  
   → 18 vs 15 → **False**

3. **“Half of 50 is 25.”**  
   → **True**

4. **“One third of 24 is 6.”**  
   → actual one third is 8 → **False**

5. **“Double of 14 is 28.”**  
   → **True**

6. **“10 plus 15 is equal to 5 plus 20.”**  
   → 25 = 25 → **True**

---

### 2. Number Properties

**Concept:** Simple properties such as even/odd, basic divisibility, last digit.

**Template examples:**

- `N is an even number.`  
- `A number that ends with D is an even/odd number.`  
- `If a number is even, then ...`

**Example items:**

1. **“14 is an even number.”**  
   → **True**

2. **“21 is an even number.”**  
   → **False**

3. **“A number that ends with 0 is an even number.”**  
   → **True**

4. **“A number that ends with 5 is an even number.”**  
   → **False**

5. **“If a number is even, then it can be divided by 2 with no remainder.”**  
   → **True**

---

### 3. Lists and Patterns

**Concept:** Recognize simple numerical patterns in a list.

**Template examples:**

- `In this list: ..., each number is K more than the number before it.`  
- `In this list: ..., each number is K less than the number before it.`  
- `In this list: ..., each number is double the number before it.`  

**Example items:**

1. **“In this list: 1, 3, 5, 7, 9, each number is 2 more than the number before it.”**  
   → **True**

2. **“In this list: 2, 4, 6, 8, 10, each number is 3 more than the number before it.”**  
   → differences are 2 → **False**

3. **“In this list: 2, 5, 8, 11, 14, each number is 3 more than the number before it.”**  
   → **True**

4. **“In this list: 9, 7, 5, 3, 1, each number is 2 less than the number before it.”**  
   → **True**

5. **“In this list: 2, 4, 8, 16, 32, each number is double the number before it.”**  
   → **True**

---

### 4. Transitive Comparisons

**Concept:** Reason about chains like “A taller than B, B taller than C.”

**Template examples:**

- `If A is [comparison] than B and B is [comparison] than C, then A is [comparison] than C.`  

**Example items:**

1. **“If A is taller than B and B is taller than C, then A is taller than C.”**  
   → **True**

2. **“If P is older than Q and Q is older than R, then R is older than P.”**  
   → **False**

3. **“If S is heavier than T and T is heavier than U, then S is heavier than U.”**  
   → **True**

4. **“If K is faster than L and L is faster than M, then K is slower than M.”**  
   → **False**

---

### 5. Set / Category Logic

**Concept:** Use made-up category names (Zors, Blins, etc.) to test logical structure, not background knowledge.

**Template examples:**

- `If all X are Y and all Y are Z, then [conclusion].`  
- `If all X are Y and some Y are Z, then [conclusion].`  
- `If no X are Y and all Y are Z, then [conclusion].`  

**Example items:**

1. **“If all Zors are Blins and all Blins are Kets, then all Zors are Kets.”**  
   → **True**

2. **“If all Rims are Laks and some Laks are Fods, then some Fods are Rims for sure.”**  
   → necessity claim is wrong → **False**

3. **“If some A are B and all B are C, then some C are A.”**  
   → **True**

4. **“If all X are Y and some Y are Z, then all Z are X.”**  
   → **False**

5. **“If no Pals are Qins and all Qins are Rels, then no Pals are Rels.”**  
   → **True**

---

### 6. Ordering / Spatial Reasoning

**Concept:** Positions in a line or row, using words like left, right, between.

**Template examples:**

- `In a row of N boxes from left to right A, B, C, ..., [statement].`  
- `In a row of seats numbered 1 to N from left to right, [statement].`  

**Example items:**

1. **“In a row of four boxes from left to right A, B, C, D, box B is between box A and box C.”**  
   → **True**

2. **“In a row of four boxes from left to right A, B, C, D, box A is between box B and box C.”**  
   → **False**

3. **“In a row of seats numbered 1 to 5 from left to right, seat 3 is between seat 2 and seat 4.”**  
   → **True**

4. **“In a row of seats numbered 1 to 5 from left to right, seat 1 is between seat 2 and seat 3.”**  
   → **False**

---

### 7. Points and Scoring Problems

**Concept:** Simple “value per symbol” rules, then compute points.

**Template examples:**

- `If X is worth P points and Y is worth Q points, then [combination] is worth R points.`  

**Example items:**

1. **“If a star is worth 3 points and a circle is worth 2 points, then two stars and one circle are worth 8 points.”**  
   → 2×3 + 2 = 8 → **True**

2. **“If a square is worth 4 points and a triangle is worth 1 point, then one square and three triangles are worth 6 points.”**  
   → 4 + 3×1 = 7 → **False**

3. **“If a diamond is worth 5 points and a heart is worth 2 points, then one diamond and two hearts are worth 9 points.”**  
   → 5 + 2×2 = 9 → **True**

---

### 8. Basic Logical Rules (If/Then/All/Some)

**Concept:** Very simple logical statements to test understanding of implication and category definitions.

**Template examples:**

- `If it is A, then it is B.`  
- `If something is X, then it has property Y.`  

**Example items:**

1. **“If a shape is a square, then it has four sides.”**  
   → **True**

2. **“If a shape has four sides, then it must be a square.”**  
   → could be rectangle, etc. → **False**

3. **“If a number is divisible by 4, then it is also divisible by 2.”**  
   → **True** (if “divisible by” is defined for users in instructions)

4. **“If a number is divisible by 2, then it is also divisible by 4.”**  
   → **False**

5. **“If it is raining, then the ground is wet.”**  
   → treated as a simple rule in the item → **True**

6. **“If the ground is wet, then it must be raining.”**  
   → other reasons for wet ground → **False**

---

## Difficulty and Item Bank Expansion

The project is designed to support **large-scale item generation**. Difficulty can be controlled by adjusting:

- **Complexity of relationships**
  - Number of steps in the reasoning (e.g., 1-step vs 2-step implications)
- **Size and range of numbers**
  - Small numbers (1–20) for easier items  
  - Larger or less “round” numbers for harder items
- **Clarity of patterns**
  - Simple, constant differences vs mixed patterns
- **Logical strength**
  - “Some” vs “all” vs “no,” and whether conclusions are necessary or merely possible

Rough distribution for a 100-item test (initial suggestion):

- 20 items – Arithmetic comparisons  
- 15 items – Number properties  
- 20 items – Lists and patterns  
- 15 items – Transitive comparisons  
- 10 items – Set/category logic  
- 10 items – Ordering/spatial  
- 10 items – Points/scoring and basic logical rules  

This can be tuned after empirical data collection.

---

## Psychometrics and Validation

To align scores with traditional IQ metrics, we will eventually need:

1. **Pilot Studies**  
   - Administer the test to a diverse sample (multiple countries, language backgrounds).  
   - Have a subset of participants also take a standard, well-validated IQ test.

2. **Item Analysis**  
   - Estimate item difficulty and discrimination (e.g., using item response theory).  
   - Remove or revise items that:
     - Are too easy or too hard  
     - Do not discriminate between higher and lower scorers  
     - Show signs of language or cultural bias

3. **Score Scaling**  
   - Convert raw scores into scaled scores and, if appropriate, IQ-like scores (e.g., mean 100, SD 15).  
   - Validate reliability (internal consistency) and test-retest stability.

4. **Bias Checks**  
   - Check for differential item functioning (DIF) across groups (e.g., different native languages, regions, genders).  
   - Flag and adjust or remove biased items.

---

## Repository Structure (Proposed)

A possible structure for this repo:

```text
.
├── README.md                 # This file
├── LICENSE                   # License information
├── data
│   ├── items_raw.json        # Raw item bank (all drafts)
│   ├── items_clean.json      # Cleaned/approved items
│   └── item_metadata.json    # Difficulty, type, status, etc.
├── docs
│   ├── language_guidelines.md   # Detailed ESL style guide
│   ├── item_templates.md        # Formal templates for generation
│   └── psychometrics_plan.md    # Analysis and validation plan
├── src
│   ├── generator
│   │   ├── arithmetic.py        # Code to generate arithmetic items
│   │   ├── patterns.py          # Code to generate pattern items
│   │   ├── logic_sets.py        # Code to generate set/category items
│   │   └── ...
│   ├── scoring
│   │   └── scoring_model.py     # Placeholder for scoring/IRT logic
│   └── ui
│       └── api_example.md       # Notes on API/UI usage
└── tests
    └── test_item_validity.py    # Tests to ensure items follow rules
```

## Contributing
------------

Contributions are welcome, especially in the following areas:

-   New **item templates** that obey:

    -   Single-sentence rule

    -   ESL-friendly language

    -   Culture-reduced content

-   **Review and editing** of existing items for:

    -   Clarity and simplicity

    -   Logical correctness

    -   Appropriate difficulty

-   **Code contributions** for:

    -   Item generation

    -   Data collection pipelines

    -   Psychometric analysis and scoring models

-   **Research contributions** to improve:

    -   Cross-cultural fairness

    -   Correlation with established IQ tests

    -   Detection and removal of biased items

When contributing, please:

1.  Follow the **language guidelines** and **design principles** in this README.

2.  Add or update tests where relevant.

3.  Include clear documentation for new item families or generation logic.
