import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    prob_dist = {}
    all_pages = list(corpus.keys())
    n_pages = len(all_pages)

    linked_pages = corpus[page]
    n_linked = len(linked_pages)

    if n_linked == 0:
        # If page has no outgoing links, choose randomly among all pages.
        for p in all_pages:
            prob_dist[p] = 1 / n_pages
    else:
        # Base probability from random choice across all pages
        random_prob = (1 - damping_factor) / n_pages
        # Probability from following a link
        link_prob = damping_factor / n_linked

        for p in all_pages:
            prob_dist[p] = random_prob

        for linked_page in linked_pages:
            prob_dist[linked_page] += link_prob

    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_counts = {page: 0 for page in corpus}
    all_pages = list(corpus.keys())

    # First sample
    current_page = random.choice(all_pages)
    page_counts[current_page] += 1

    # Generate remaining n-1 samples
    for _ in range(n - 1):
        # Get transition model for the current page
        trans_model = transition_model(corpus, current_page, damping_factor)

        # Get pages and their probabilities
        pages = list(trans_model.keys())
        probabilities = list(trans_model.values())

        # Choose the next page based on the distribution
        current_page = random.choices(pages, weights=probabilities, k=1)[0]
        page_counts[current_page] += 1

    # Calculate PageRank as proportions
    pagerank = {page: count / n for page, count in page_counts.items()}

    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    num_pages = len(corpus)

    # Initialize PageRank for all pages to 1/N
    pagerank = {page: 1 / num_pages for page in corpus}

    # A page that has no links should be interpreted as having one link for every page in the corpus
    modified_corpus = {}
    all_pages_set = set(corpus.keys())
    for page, links in corpus.items():
        if not links:
            modified_corpus[page] = all_pages_set
        else:
            modified_corpus[page] = links

    while True:
        new_pagerank = {}
        for page in corpus:
            # First part of the formula
            rank = (1 - damping_factor) / num_pages
            
            # Second part of the formula
            sum_val = 0
            for i in corpus:
                # If page i links to the current page
                if page in modified_corpus[i]:
                    num_links = len(modified_corpus[i])
                    sum_val += pagerank[i] / num_links
            
            rank += damping_factor * sum_val
            new_pagerank[page] = rank

        # Check for convergence
        max_change = 0
        for page in corpus:
            change = abs(pagerank[page] - new_pagerank[page])
            if change > max_change:
                max_change = change
        
        pagerank = new_pagerank
        
        if max_change < 0.001:
            break
    
    # Normalize final ranks to ensure they sum to 1
    total_rank = sum(pagerank.values())
    if total_rank != 0:
        for page in pagerank:
            pagerank[page] /= total_rank
            
    return pagerank


if __name__ == "__main__":
    main()
