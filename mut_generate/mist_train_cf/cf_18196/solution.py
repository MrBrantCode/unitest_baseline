"""
QUESTION:
Calculate the sum of an array of float values, excluding any negative values and values greater than 100, and round the final sum to two decimal places. Implement this logic in a function named `calculate_sum` that takes an array as an input.
"""

def calculate_sum(arr):
    total_sum = 0

    for num in arr:
        if num > 0 and num <= 100:
            total_sum += num

    return round(total_sum, 2)