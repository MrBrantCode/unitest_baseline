"""
QUESTION:
Create a function named `calculate_sum` that takes an array of numbers as input, calculates the sum of all numbers, counts the number of positive numbers, and counts the number of negative numbers. The function should return three values: the count of positive numbers, the count of negative numbers, and the total sum. The function must be able to handle arrays containing negative numbers and must be efficient enough to handle large input arrays.
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