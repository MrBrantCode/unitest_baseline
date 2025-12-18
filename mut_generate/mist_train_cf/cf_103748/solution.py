"""
QUESTION:
Write a function named `sum_divisible_by_three` that takes a list of integers as input and returns the sum of all numbers in the list that are greater than 10 and divisible by 3.
"""

def sum_divisible_by_three(my_list):
    return sum(item for item in my_list if item > 10 and item % 3 == 0)