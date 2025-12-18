"""
QUESTION:
Write a function `jaccard_distance` that calculates the sum of Jaccard distances between two lists of sets. The Jaccard distance is a measure of dissimilarity between two sets, and is defined as 1 - (the size of intersection / size of union of the two sets). The function should take two lists of sets as input and return the sum of Jaccard distances. The order of sets in both lists is significant.
"""

def jaccard_distance(set1, set2):
    intersection_len = len(set1.intersection(set2))
    union_len = len(set1.union(set2))
    return 1 - (intersection_len / union_len)