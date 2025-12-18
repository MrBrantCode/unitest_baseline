"""
QUESTION:
Create a function `sum_even_numbers` that takes an array of at least 10 positive integers in ascending order and returns the sum of all even numbers in the array. The array must contain at least 10 positive integers.
"""

def sum_even_numbers(arr):
    """Returns the sum of all even numbers in the array"""
    even_sum = 0
    for num in arr:
        if num % 2 == 0:
            even_sum += num
    return even_sum