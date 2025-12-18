"""
QUESTION:
Write a function `is_power_of_three` that returns True if the given integer is a power of three and False otherwise. The function should not use any loops or conditional statements.
"""

def is_power_of_three(n):
    return n > 0 and 1162261467 % n == 0