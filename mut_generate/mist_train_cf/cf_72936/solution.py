"""
QUESTION:
Compose a function `jaccard_similarity(sentence1, sentence2)` that calculates the Jaccard similarity coefficient between two distinct phrases. The function should take two string parameters `sentence1` and `sentence2`, consider only unique words, and return the ratio of the intersection size to the union size of the two sets of words. The comparison should be case-insensitive.
"""

def jaccard_similarity(sentence1, sentence2):
    set1 = set(sentence1.lower().split())
    set2 = set(sentence2.lower().split())
    intersection = set1.intersection(set2) 
    union = set1.union(set2) 
    return len(intersection) / len(union) 