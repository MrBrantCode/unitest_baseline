"""
QUESTION:
Write a function named `sum_positive_numbers` that takes a list of integers as input and returns the sum of all positive numbers in the list. The function must have a time complexity of O(n), where n is the length of the input list.
"""

def sum_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total