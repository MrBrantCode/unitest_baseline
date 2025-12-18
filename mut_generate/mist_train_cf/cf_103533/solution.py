"""
QUESTION:
Write a function named `compute_average` that calculates the average of all positive integers in a given array `arr`. The array `arr` contains a maximum of 1000 integers between -100 and 100. If `arr` does not contain any positive numbers, the function should return 0.
"""

def compute_average(arr):
    positive_nums = [num for num in arr if num > 0]
    if len(positive_nums) == 0:
        return 0
    return sum(positive_nums) / len(positive_nums)