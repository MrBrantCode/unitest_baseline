"""
QUESTION:
Create a function named `partition_and_sort` that takes a list of floating-point numbers as input. The function should group the numbers into three categories (negative, zero, and positive), sort each group in ascending order, and return a combined list with the sorted negative numbers, zeros, and positive numbers in that order. The function should have a time complexity of O(n log n).
"""

def partition_and_sort(numbers):
    # Initialize lists for different categories
    negatives, zeros, positives = [], [], []

    # Partition numbers into different lists
    for num in numbers:
        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)
        else:
            zeros.append(num)

    # Sort each list
    negatives.sort()
    positives.sort()

    # Combine sorted lists
    result = negatives + zeros + positives

    return result