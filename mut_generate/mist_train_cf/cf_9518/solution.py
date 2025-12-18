"""
QUESTION:
Write a function `is_triangle_number` that takes an integer greater than or equal to 1 as input and returns True if the number is a triangle number and False otherwise. A triangle number is a number that can be represented as the sum of consecutive positive integers starting from 1.
"""

def is_triangle_number(n):
    sum = 0
    i = 1
    while sum < n:
        sum += i
        i += 1
    return sum == n