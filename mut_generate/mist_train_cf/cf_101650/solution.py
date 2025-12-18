"""
QUESTION:
Write a function `sort_evens_descending` that takes an array of integers as input, removes all odd numbers, and returns the remaining even numbers in descending order. The function should handle arrays of any length.
"""

def sort_evens_descending(arr):
    evens = [num for num in arr if num % 2 == 0]
    evens.sort(reverse=True)
    return evens