"""
QUESTION:
Classify all elements in a given integer array as 'even' or 'odd' and return the classification as a list of strings. Implement a function named classify_numbers that takes a list of integers as input and returns a list of strings where each string is either 'even' or 'odd' corresponding to the elements in the input list.
"""

def classify_numbers(nums):
    return ['even' if num % 2 == 0 else 'odd' for num in nums]