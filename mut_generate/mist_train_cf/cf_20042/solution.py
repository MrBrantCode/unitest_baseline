"""
QUESTION:
Write a function called `get_sorted_unique_evens` that takes a list of integers as input. The function should return a new list containing only the even numbers from the input list, sorted in ascending order, with no duplicates. The solution should have a time complexity of O(n log n) or better.
"""

def get_sorted_unique_evens(input_list):
    evens = sorted(set(num for num in input_list if num % 2 == 0))
    return evens