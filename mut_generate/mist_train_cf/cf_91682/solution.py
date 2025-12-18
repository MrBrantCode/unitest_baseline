"""
QUESTION:
Write a function named `sum_exclude_multiples_of_three` that takes a list of numbers as input and returns the sum of the numbers in the list excluding any numbers that are multiples of 3.
"""

def sum_exclude_multiples_of_three(numbers):
    sum = 0
    for num in numbers:
        if num % 3 != 0:
            sum += num
    return sum