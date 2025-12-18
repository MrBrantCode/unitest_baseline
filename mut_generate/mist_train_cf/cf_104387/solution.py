"""
QUESTION:
Write a function `find_index(array, target)` that takes an array of strings and a target string as input, and returns the index of the first occurrence of the target string in the array. If the target string is not found, return -1. The function should be able to handle large inputs efficiently, where the array has at least 1000 elements and the target string is at least 100 characters long and contains only lowercase letters.
"""

def find_index(array, target):
    hash_table = {}
    for i, string in enumerate(array):
        hash_table[string] = i
    if target in hash_table:
        return hash_table[target]
    else:
        return -1