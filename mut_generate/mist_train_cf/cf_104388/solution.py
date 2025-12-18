"""
QUESTION:
Create a function called `sum_of_list` that takes a list of numbers as input and returns the sum of the numbers in the list, excluding any numbers that are multiples of 3 and ignoring any negative numbers.
"""

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        if num >= 0 and num % 3 != 0:
            total += num
    return total