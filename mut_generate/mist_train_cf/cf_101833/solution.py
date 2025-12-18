"""
QUESTION:
Write a function `sort_evens_descending` that takes a list of integers as input, removes all odd numbers from the list, and returns the remaining even numbers in descending order.
"""

def sort_evens_descending(arr):
    evens = [num for num in arr if num % 2 == 0]
    evens.sort(reverse=True)
    return evens