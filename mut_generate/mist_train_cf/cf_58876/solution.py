"""
QUESTION:
Write a function `product_of_uniques` that takes a sequence of integers as input and returns the product of all unique numbers in the sequence. The function should ignore duplicate numbers and only consider distinct numbers in the calculation.
"""

def product_of_uniques(seq):
    product = 1
    unique_numbers = set(seq)
    for number in unique_numbers:
        product *= number
    return product