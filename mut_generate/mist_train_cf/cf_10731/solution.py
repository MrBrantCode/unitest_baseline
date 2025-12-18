"""
QUESTION:
Write a function named `remove_duplicates_and_sort` that takes a list of numbers as input, removes duplicates, and returns the remaining elements in descending order. The function should have a time complexity of O(n log n).
"""

def remove_duplicates_and_sort(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    return unique_numbers