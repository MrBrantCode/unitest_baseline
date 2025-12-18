"""
QUESTION:
Write a function `is_strictly_ascending` to determine if a given list of integers is strictly ascending. A list is strictly ascending if each element is greater than the previous element. The input list will contain at least two elements.
"""

def is_strictly_ascending(lst):
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))