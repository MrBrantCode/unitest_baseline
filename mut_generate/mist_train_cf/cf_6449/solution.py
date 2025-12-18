"""
QUESTION:
Write a function named `symmetric_difference(set1, set2)` that takes two sets as input and returns a new set containing the symmetric difference of the input sets, with a time complexity of O(n), where n is the total number of elements in both input sets. The symmetric difference of two sets A and B is defined as the set of elements that are in either A or B, but not in both.
"""

def symmetric_difference(set1, set2):
    result = set()
    for element in set1:
        if element not in set2:
            result.add(element)
    for element in set2:
        if element not in set1:
            result.add(element)
    return result