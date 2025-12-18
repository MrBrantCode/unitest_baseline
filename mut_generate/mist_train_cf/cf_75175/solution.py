"""
QUESTION:
Create a function called `sum_greater_nums` that takes an array of numbers and a number as arguments, and returns the sum of all numbers in the array that are greater than the given number.
"""

def sum_greater_nums(arr, num):
    return sum([i for i in arr if i > num])