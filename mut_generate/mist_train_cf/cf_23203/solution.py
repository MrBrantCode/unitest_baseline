"""
QUESTION:
Implement the function `calculate_sum()` that takes in a list of numbers as a parameter and returns the sum of the numbers using recursion. The list may be empty and should not contain any negative numbers. If negative numbers are present, replace them with 0 before calculating the sum.
"""

def calculate_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        if numbers[0] < 0:
            numbers[0] = 0
        return numbers[0] + calculate_sum(numbers[1:])