"""
QUESTION:
Write a function named `sum_even_elements` that takes an array of at least 10 positive integers as input, and returns the sum of all even elements in the array using a for loop.
"""

def sum_even_elements(arr):
    sum_even = 0
    for num in arr:
        if num % 2 == 0:
            sum_even += num
    return sum_even