"""
QUESTION:
Implement the function `calculate_sum()` that takes in a list of non-negative numbers as a parameter and returns the sum of the numbers using recursion. If the input list contains any negative numbers, consider them as 0 for the sum calculation. The function should also handle empty lists and return 0 in such cases.
"""

def calculate_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        if numbers[0] < 0:
            numbers[0] = 0
        return numbers[0] + calculate_sum(numbers[1:])