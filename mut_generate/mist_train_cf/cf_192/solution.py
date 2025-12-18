"""
QUESTION:
Write a function `sum_of_largest_two` that takes a list of numbers as input. The function should sort the list in descending order and return the sum of the first two elements. The input list will contain at least two elements.
"""

def sum_of_largest_two(numbers):
    numbers.sort(reverse=True)
    return numbers[0] + numbers[1]