"""
QUESTION:
Implement a function `symmetric_difference(set1, set2)` that takes two sets as input, each containing between 20 and 30 positive integers between 1 and 10000. The function should return a set containing the symmetric difference of `set1` and `set2`, i.e., the elements present in either `set1` or `set2`, but not in both. The function should have a time complexity of O(n), where n is the total number of elements in both sets.
"""

def symmetric_difference(set1, set2):
    symmetric_diff = set()

    for element in set1:
        if element not in set2:
            symmetric_diff.add(element)

    for element in set2:
        if element not in set1:
            symmetric_diff.add(element)

    return symmetric_diff