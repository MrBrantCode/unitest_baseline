"""
QUESTION:
Create a function named `sort_strings` that takes a list of strings as input and returns the list sorted in the following order: 
- by the length of the strings in descending order, and 
- for strings with equal length, by the sum of their ASCII values in descending order.
"""

def sort_strings(lst):
    return sorted(lst, key=lambda x: (-len(x), -sum(map(ord, x))))