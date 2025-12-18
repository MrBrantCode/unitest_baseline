"""
QUESTION:
Write a function named `calculate_median` that takes an array of integers as input and returns the median of the array. The array may contain both positive and negative integers, and it may be unsorted, contain duplicates, or be sorted in descending order. The function should handle cases where the length of the array is odd or even, and return a single number representing the median.
"""

def calculate_median(array):
    sorted_array = sorted(array)
    length = len(sorted_array)
    
    if length % 2 == 1:
        return sorted_array[length // 2]
    else:
        mid1 = sorted_array[length // 2]
        mid2 = sorted_array[length // 2 - 1]
        return (mid1 + mid2) / 2