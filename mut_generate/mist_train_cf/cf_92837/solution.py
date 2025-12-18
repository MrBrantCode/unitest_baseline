"""
QUESTION:
Write a function `sort_strings` that takes a list of tuples of two strings each, and returns the list sorted in descending order based on the sum of the ASCII values of each character in the key and the value.
"""

def sort_strings(string_list):
    return sorted(string_list, key=lambda x: sum(ord(c) for c in x[0] + x[1]), reverse=True)