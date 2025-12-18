"""
QUESTION:
Write a function `sum_even_numbers` that takes a list of integers as input and returns the sum of all even numbers in the list. The function should have a time complexity of O(n) and should not use any built-in sum functions or external libraries.
"""

def sum_even_numbers(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total