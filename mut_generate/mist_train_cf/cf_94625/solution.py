"""
QUESTION:
Write a function `sort_rows` that takes a two-dimensional array `arr` as input and returns the array with rows sorted in descending order based on their sums, ignoring any rows that contain negative numbers.
"""

def sort_rows(arr):
    return sorted((row for row in arr if all(num >= 0 for num in row)), key=sum, reverse=True)