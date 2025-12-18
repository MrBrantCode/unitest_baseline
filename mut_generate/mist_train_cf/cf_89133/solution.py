"""
QUESTION:
Implement a function named sort_strings that takes a list of strings as input, sorts them by their length in descending order, and if two or more strings have the same length, sorts them in lexicographically ascending order. The input list contains only unique strings with lowercase alphabets, and each string's length does not exceed 1000 characters. The total number of characters in all the strings combined does not exceed 10^9. The function should have a time complexity of O(n log n).
"""

def sort_strings(strings):
    return sorted(strings, key=lambda s: (-len(s), s))