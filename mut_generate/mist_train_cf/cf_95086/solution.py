"""
QUESTION:
Write a function `calculate_sum(arr)` that calculates the sum of the elements of an array `arr` containing float values. The function should exclude any negative values and values greater than 100, then round the final sum to two decimal places.
"""

def calculate_sum(arr):
    total_sum = 0

    for num in arr:
        if num > 0 and num <= 100:
            total_sum += num

    return round(total_sum, 2)