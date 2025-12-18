"""
QUESTION:
Write a function named `calculate_product` that takes a sequence of integers and an integer `n` as input. The function should return the product of all unique numbers in the sequence that are not multiples of `n`.
"""

def calculate_product(sequence, n):
    numbers = set(sequence)  # To get unique elements
    product = 1  # Initialize product
    for number in numbers:
        # Exclude the number if it is multiple of 'n' 
        if number % n != 0:
            product *= number
    return product