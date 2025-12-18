"""
QUESTION:
Create a function named `filter_sort` that takes a list of integers as input, returns a new list containing only the even numbers from the original list, removes any duplicates from the resulting list, and sorts it in descending order.
"""

def filter_sort(lst):
    even_numbers = list(set(filter(lambda x: x % 2 == 0, lst)))
    even_numbers.sort(reverse=True)
    return even_numbers