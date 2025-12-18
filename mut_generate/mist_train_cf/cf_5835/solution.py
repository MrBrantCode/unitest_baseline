"""
QUESTION:
Implement the `sort_strings` function that takes a list of unique strings containing only lowercase alphabets, with each string not exceeding 1000 characters and the total number of characters not exceeding 10^9. Sort the strings by their length in descending order, and if two or more strings have the same length, sort them in lexicographically ascending order. The function should have a time complexity of O(n log n).
"""

def sort_strings(strings):
    key = lambda s: (-len(s), s)
    return sorted(strings, key=key)