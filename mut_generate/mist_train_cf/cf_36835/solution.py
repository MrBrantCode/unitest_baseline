"""
QUESTION:
Create a function `sum_even_numbers` that takes a list of integers as input and returns the sum of all the even numbers in the list. The function must not use any conditional statements (if, else, etc.) or the modulo operator (%).
"""

def sum_even_numbers(nums):
    total_sum = 0
    for num in nums:
        total_sum += (1 - (num & 1)) * num
    return total_sum