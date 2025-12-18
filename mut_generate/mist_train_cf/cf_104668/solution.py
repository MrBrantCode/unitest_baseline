"""
QUESTION:
Write a function named count_unique_positive_elements that takes an array of integers as input, and returns the number of unique positive integers in the array after sorting it in non-decreasing order.
"""

def count_unique_positive_elements(arr):
    return len(set([x for x in arr if x > 0]))