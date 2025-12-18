"""
QUESTION:
Write a function `sort_tuples(lst)` that takes a list of tuples as input and returns a new list with the tuples sorted in descending order based on their second element. The function should use a stable sorting algorithm, have a time complexity of O(n log n), and use a limited amount of additional space.
"""

def sort_tuples(lst):
    return sorted(lst, key=lambda x: x[1], reverse=True)