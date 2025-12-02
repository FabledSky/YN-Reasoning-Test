# Psychometrics Plan

A concise plan for piloting, analyzing, and calibrating the Yes/No reasoning test.

**Status note:** The assessment is in a research phase and should not be used for hiring, diagnosis, or other high-stakes decisions until validation is complete.

## Pilot Study Steps
- Recruit a **diverse sample** across regions, native languages, and genders; aim for parallel groups to check bias.
- Collect **demographics** (age, gender, language background) for DIF analysis; record test form identifiers.
- Administer the **full 100-item form** under consistent timing; randomize item order to limit position effects.
- For a subset of participants, collect scores from a **benchmark cognitive measure** to support validity checks.

## Item Analysis
- Compute **classical stats** per item: proportion correct, point-biserial discrimination, and response time distribution.
- Fit **IRT models** (1PL/2PL) to estimate difficulty and discrimination; flag items with low information.
- Inspect **local dependence** (residual correlations) to avoid overlapping content or chained reasoning.
- Track revisions: items that are too easy/hard or that miskey should be rewritten using the templates.

## Differential Item Functioning (DIF)
- Run **Mantel–Haenszel** or logistic regression DIF across key groups (native vs non-native English, region, gender).
- Use **effect size thresholds** (e.g., ETS classification) to flag moderate or large DIF for review.
- Review flagged items for **language complexity, cultural references, or numeric range** that might drive bias.
- Retest revised items in a follow-up pilot to confirm DIF reduction.

## Scoring Calibration
- Anchor the score scale using **IRT estimates**: set mean difficulty near zero and scale to desired variance.
- Convert raw scores to **scaled scores** (e.g., mean 100, SD 15) once sample size is stable.
- Evaluate **reliability** (Cronbach’s alpha, IRT information) and **test–retest stability** on repeat takers.
- Correlate test scores with **external measures** to monitor convergent validity and adjust item mix if needed.
