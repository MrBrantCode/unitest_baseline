"""
QUESTION:
Implement a function named `jaccard_similarity(sentence1, sentence2)` that calculates the Jaccard similarity coefficient between two input sentences. The function should split the sentences into sets of words and return the ratio of the size of the intersection to the size of the union of the two sets. Assume that the input sentences only contain spaces as word separators and do not contain punctuation marks.
"""

def jaccard_similarity(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)