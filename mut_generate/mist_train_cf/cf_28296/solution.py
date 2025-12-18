"""
QUESTION:
Implement a function `sum_of_even_numbers` that calculates the sum of all even numbers in a given list of integers. The function should take a list of integers as input and return the sum of all the even numbers in the list. The input list may contain both positive and negative integers, and may be empty.
"""

def sum_of_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum