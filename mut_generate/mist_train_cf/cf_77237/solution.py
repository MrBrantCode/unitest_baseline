"""
QUESTION:
Write a function `find_groups(lst, threshold)` that returns a list of all distinct groups of three numbers in the input list `lst` that have a product greater than the given `threshold`. The function should handle both positive and negative numbers and consider the case where the list doesn't contain enough numbers. If the list has less than three elements, the function should return an empty list.
"""

from itertools import combinations

def find_groups(lst, threshold):
    if len(lst) < 3:
        return []

    triplets = []
    for group in combinations(lst, 3):
        if group[0] * group[1] * group[2] > threshold:
            triplets.append(list(group))
    return triplets