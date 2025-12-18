"""
QUESTION:
Write a function `count_positive_numbers` that takes a list of integers as input and returns the number of positive integers in the list.
"""

def count_positive_numbers(input_numbers):
    positive_numbers = 0
    for num in input_numbers:
        if num > 0:
            positive_numbers += 1
    return positive_numbers