"""
QUESTION:
Implement a function named `descending_order` that takes a list of strings as input. The function should verify if the list is in descending alphabetical order, ignoring case sensitivity, special characters, and numbers. If the list is not in descending order, the function should sort it using a manual sorting algorithm (without using Python's built-in sort() function or any other sorting functions available in Python libraries).
"""

import re

def descending_order(lst):
    def clean_string(s):
        return re.sub(r'\W+|\d+', '', s).lower()

    n = len(lst)
    # Bubble sort
    for i in range(n):
        for j in range(0, n-i-1):
            if clean_string(lst[j]) < clean_string(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst