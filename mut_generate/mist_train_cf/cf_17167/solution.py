"""
QUESTION:
Write a function `string_lengths` that takes a list of strings as input and returns a new list containing the lengths of each string. Implement this function without using built-in string manipulation methods such as `len()` or string slicing, and ensure a time complexity of O(n), where n is the total number of characters in all the strings combined.
"""

def string_lengths(strings):
    lengths = []
    for string in strings:
        count = 0
        for char in string:
            count += 1
        lengths.append(count)
    return lengths