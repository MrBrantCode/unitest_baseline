"""
QUESTION:
Create a function named `calculate_sum` that takes an array of numbers as input. The function should return three values: the count of positive numbers in the array, the count of negative numbers, and the sum of all numbers. The function should handle large input arrays efficiently and correctly process negative numbers.
"""

def calculate_sum(arr):
    positive_count = 0
    negative_count = 0
    total_sum = 0

    for num in arr:
        if num >= 0:
            positive_count += 1
        else:
            negative_count += 1
        total_sum += num

    return positive_count, negative_count, total_sum