"""
QUESTION:
Write a function `find_unique_pairs` that generates all unique pairs from a given list of integers in ascending order, without using built-in functions or libraries that directly solve the problem. The function should have a time complexity of O(n^2), handle larger input sizes efficiently, and work with negative numbers and duplicate elements in the list. Note that pairs with the same elements but in reverse order are considered duplicates and should not be included.
"""

def find_unique_pairs(lst):
    pairs = set()
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            pair = (lst[i], lst[j])
            pairs.add(pair)
    return sorted(list(pairs))