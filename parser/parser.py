import nltk
import sys
import string

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> PART | PART Conj PART
PART -> NP VP | NP Adv VP | VP
NP -> N | NA N
NA -> Det | Adj | NA NA
VP -> V | V SUPP
SUPP -> NP | P | Adv | SUPP SUPP | SUPP SUPP SUPP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()
    else:
        s = input("Sentence: ")

    s = preprocess(s)

    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    sentence = sentence.lower()
    tokens = sentence.split()
    result = []
    for token in tokens:
        token = token.strip(string.punctuation)
        if any(c.isalpha() for c in token):
            result.append(token)
    return result


def np_chunk(tree):
    chunks = []
    for subtree in tree.subtrees(lambda t: t.label() == "NP"):
        has_inner_np = any(
            child is not subtree and child.label() == "NP"
            for child in subtree.subtrees()
        )
        if not has_inner_np:
            chunks.append(subtree)
    return chunks


if __name__ == "__main__":
    main()
