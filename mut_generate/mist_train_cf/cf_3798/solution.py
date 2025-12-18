"""
QUESTION:
Write a function named `sum_even_numbers` that takes a list of integers as input and returns the sum of all even numbers in the list. The function should use recursion and have a time complexity of O(n), where n is the number of elements in the list. Do not use list comprehension or lambda functions.
"""

def sum_even_numbers(lst):
    if len(lst) == 0:
        return 0
    if lst[0] % 2 == 0:
        return lst[0] + sum_even_numbers(lst[1:])
    else:
        return sum_even_numbers(lst[1:])