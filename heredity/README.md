# Project 2: Heredity

## My Learning Journey

This one hurt my brain a little. Probability is tricky because it's so easy to be *slightly* wrong.

The concept of a "Joint Probability" clicked when I realized I just needed to multiply the probabilities of every unrelated event together.
*   Prob(Mother has gene) * Prob(Father passes gene) * Prob(Child gets trait)...

The hardest part was the **Normalization**. After you sum up all the "True" cases and "False" cases, they rarely add up to exactly 1.0 because we're only looking at a slice of the data. Rescaling them so they equal 100% was a crucial final step I kept missing at first.
