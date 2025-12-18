"""
QUESTION:
Write a function `extract_values(dictionary)` that takes a dictionary as input and returns a list of its values that are greater than 5 and less than 9. The returned list should be in ascending order. The time complexity of the solution should be O(nlogn), where n is the total number of values in the dictionary.
"""

def entance(dictionary):
    return sorted([value for value in dictionary.values() if 5 < value < 9])