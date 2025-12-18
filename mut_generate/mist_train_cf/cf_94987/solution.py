"""
QUESTION:
Implement a function `find_index(array, target)` that finds the first index of a given `target` string in a large array of strings. If the `target` string is not found, return -1. The input `array` has at least 1000 elements and the `target` string is at least 100 characters long and contains only lowercase letters. The function should have a time complexity of O(n), where n is the number of elements in the array.
"""

def find_index(array, target):
    hash_table = {}
    for i, string in enumerate(array):
        hash_table[string] = i
    return hash_table.get(target, -1)