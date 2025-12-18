"""
QUESTION:
Write a function named `find_largest_numbers` that takes a list of integers as input, excludes any negative numbers, and returns the largest number. If all input numbers are negative, return an empty list. The function should have a time complexity of O(n log n) and be able to handle input numbers up to a maximum value of 10^9.
"""

def find_largest_numbers(numbers):
    positives = [num for num in numbers if num >= 0]
    if not positives:
        return []
    positives.sort(reverse=True)
    return positives[0]