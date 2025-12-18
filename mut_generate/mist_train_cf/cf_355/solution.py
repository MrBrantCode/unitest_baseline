"""
QUESTION:
Write a function named find_sum that calculates the sum of elements in a list until it encounters a positive number. The function should take a list of numbers as input and return the sum of the elements before the first positive number. Assume the input list contains at least one positive number.
"""

def find_sum(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            break
        total += num
    return total