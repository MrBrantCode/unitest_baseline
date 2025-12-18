"""
QUESTION:
Write a function called 'calculate_statistics' that takes an array of numbers as input and returns the total, average, and median of the array. The median is the middle element if the array has an odd length, and the average of the two middle elements if the array has an even length.
"""

import statistics

def calculate_statistics(arr):
    total = sum(arr)
    average = total / len(arr)
    median = statistics.median(arr)
    return total, average, median