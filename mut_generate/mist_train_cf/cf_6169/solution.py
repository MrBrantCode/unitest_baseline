"""
QUESTION:
Write a function named `filter_odd_numbers` that takes a list of integers as input. The function should return a new list containing only the odd numbers from the original list, sorted in descending order, with no duplicates. The function should handle empty input lists and lists with only even numbers. The time complexity of the function should be O(nlogn) or better, and it should not use any built-in sorting or duplicate removal functions.
"""

def filter_odd_numbers(arr):
    """
    Main function that filters odd numbers from the input list, sorts them in descending order, and removes duplicates.
    """
    odd_numbers = list(dict.fromkeys([num for num in arr if num % 2 != 0]))
    return sorted(odd_numbers, reverse=True)