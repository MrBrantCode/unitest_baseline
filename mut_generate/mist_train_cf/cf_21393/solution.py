"""
QUESTION:
Write a function `calculate_sum_of_even_numbers` that calculates the sum of even numbers in an array of at least 10 positive integers. The function should use a single loop to iterate through the array and must not use any built-in array manipulation functions or libraries.
"""

def calculate_sum_of_even_numbers(arr):
    total_sum = 0
    for num in arr:
        if num % 2 == 0:
            total_sum += num
    return total_sum