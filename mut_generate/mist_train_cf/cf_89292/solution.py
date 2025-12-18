"""
QUESTION:
Write a function `filter_odd_numbers(arr)` that takes a list of integers as input and returns a new list containing only the unique odd numbers in the original list in descending order. The function should have a time complexity of O(nlogn) or better and should not use any built-in sorting or duplicate removal functions. If the input list is empty or contains only even numbers, the function should return an empty list.
"""

def filter_odd_numbers(arr):
    """
    Function that filters odd numbers from the input list, sorts them in descending order, and removes duplicates.
    """
    odd_numbers = [num for num in arr if num % 2 != 0]
    odd_numbers = sorted(set(odd_numbers), reverse=True)
    return odd_numbers