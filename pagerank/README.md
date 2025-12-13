# Project 2: PageRank

## My Learning Journey

It was fascinating to see how the two methods (Sampling vs. Math) converged to the exact same numbers.

- **Sampling** felt like a Monte Carlo simulation. It was messy but intuitive. "If I just walk around random links for a million years, where do I spend the most time?"
- **Iterative** was cleaner but required being very careful with the floating-point math.

One specific bug I fought: dealing with "sink" pages (pages with no outgoing links). If you aren't careful, the probability mass just disappears into a black hole. I had to treat those pages as if they linked to *every* page efficiently. I was very excited to implement the algorithm which acts as a basis of our beloved **Google** search engine.
