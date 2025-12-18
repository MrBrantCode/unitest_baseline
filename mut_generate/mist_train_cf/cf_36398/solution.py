"""
QUESTION:
Implement the `sum_even_numbers` function, which takes a list of integers as input and returns the sum of all even numbers in the list.
"""

def sum_even_numbers(nums):
    return sum(num for num in nums if num % 2 == 0)