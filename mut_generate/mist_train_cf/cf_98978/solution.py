"""
QUESTION:
Write a function `find_largest_square_divisible` that takes a list of integers as input. The function should return the largest perfect square number in the list that is divisible by the sum of the digits of the smallest number in the list. If no such number exists, return "No valid number found". The function should handle negative integers in the list.
"""

import math
def find_largest_square_divisible(numbers):
    # Find the smallest number in the list
    smallest = min(numbers)
    # Compute the sum of its digits
    digits_sum = sum(int(digit) for digit in str(abs(smallest)) if digit.isdigit())
    # Filter the list to keep only integers that are perfect squares and divisible by digits_sum
    valid_numbers = [n for n in numbers if n > 0 and math.isqrt(n)**2 == n and n % digits_sum == 0]
    # If there are no valid numbers, return an error message
    if not valid_numbers:
        return "No valid number found"
    # Otherwise, return the largest valid number
    return max(valid_numbers)