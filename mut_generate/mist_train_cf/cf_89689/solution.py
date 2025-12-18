"""
QUESTION:
Write a function `lexicographical_order(arr)` that takes an array of strings as input, removes duplicates, and returns the unique strings in lexicographical order in descending order. The input array may contain a maximum of 10^6 strings.
"""

def lexicographical_order(arr):
    unique_strings = set(arr)
    sorted_strings = sorted(unique_strings, reverse=True)
    return sorted_strings