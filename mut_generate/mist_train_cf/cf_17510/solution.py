"""
QUESTION:
Write a Python function `filter_sort` that takes a list of integers as input. The function should return a new list containing only the even numbers from the original list, with no duplicates, and sorted in descending order.
"""

def filter_sort(lst):
    even_numbers = list(set(filter(lambda x: x % 2 == 0, lst)))
    even_numbers.sort(reverse=True)
    return even_numbers