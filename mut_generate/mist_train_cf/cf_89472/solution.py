"""
QUESTION:
Create a function named `remove_even_numbers` that takes an array of integers as input. The function should remove all even numbers from the array and return the product of the remaining numbers.
"""

def remove_even_numbers(arr):
    product = 1
    for num in arr:
        if num % 2 != 0:
            product *= num
    return product