"""
QUESTION:
Write a function `sort_strings` that sorts a list of tuples of two strings in descending order based on the sum of ASCII values of all characters in each tuple. The function should take a list of tuples as input and return the sorted list.
"""

def sort_strings(string_list):
    return sorted(string_list, key=lambda x: sum(ord(c) for c in x[0]) + sum(ord(c) for c in x[1]), reverse=True)