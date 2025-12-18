"""
QUESTION:
Write a function named `sum_positive_numbers` that calculates the sum of all positive integers in a given list of integers. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def sum_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total