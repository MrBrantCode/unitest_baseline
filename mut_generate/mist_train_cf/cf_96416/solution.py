"""
QUESTION:
Write a function called `find_largest_smallest` that takes a list of integers as input, returns the largest and smallest numbers in the list, and has a time complexity of O(n log n).
"""

def find_largest_smallest(numbers):
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)

    # The first element in the sorted list is the smallest number
    smallest = sorted_numbers[0]

    # The last element in the sorted list is the largest number
    largest = sorted_numbers[-1]

    return largest, smallest