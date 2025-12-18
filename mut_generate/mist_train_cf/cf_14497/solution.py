"""
QUESTION:
Write a function `sum_positive_numbers` that takes a list of integers as input and returns the sum of all positive numbers in the list. The solution should have a time complexity of O(n), where n is the length of the input list, and should not use built-in functions like `sum` or explicit iteration tools like `for` or `while` loops.
"""

from functools import reduce

def sum_positive_numbers(numbers):
    if not numbers:
        return 0
    
    positive_numbers = filter(lambda x: x > 0, numbers)
    return reduce(lambda x, y: x + y, positive_numbers)