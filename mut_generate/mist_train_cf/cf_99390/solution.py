"""
QUESTION:
Create a function `find_largest_square_divisible` that takes a list of integers as input. The function should return the largest number that is both a perfect square and divisible by the sum of the digits of the smallest number in the list. If no such number exists, the function should return the error message "No valid number found".
"""

import math
def find_largest_square_divisible(numbers):
    smallest = min(numbers)
    digits_sum = sum(int(digit) for digit in str(abs(smallest)) if digit.isdigit())
    valid_numbers = [n for n in numbers if n > 0 and math.isqrt(n)**2 == n and n % digits_sum == 0]
    if not valid_numbers:
        return "No valid number found"
    return max(valid_numbers)