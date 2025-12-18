"""
QUESTION:
The function should be named "calculate_average". It should take an array of integers as input and return the average of the integers rounded to the nearest integer. The array will contain at least 5 elements and at most 100 elements, and each element will be a positive integer between 1 and 1000, inclusive.
"""

def calculate_average(arr):
    return round(sum(arr) / len(arr))