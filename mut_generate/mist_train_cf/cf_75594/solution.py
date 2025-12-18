"""
QUESTION:
Write a function `get_odd_numbers_and_sums` that takes two non-negative integers `start` and `end` as input, representing a range, and does the following: 
- calculates the list of odd numbers within the range from `start` to `end` (inclusive), 
- calculates the sum of the odd numbers in the range, 
- calculates the sum of the squares of the odd numbers in the range, and 
- returns or prints these values.
The input range should be valid, i.e., `end` should be greater than or equal to `start`.
"""

def get_odd_numbers_and_sums(start, end):
    odd_numbers = [i for i in range(start, end + 1) if i % 2 != 0]
    odd_sum = sum(odd_numbers)
    odd_squares_sum = sum([i**2 for i in odd_numbers])
    return odd_numbers, odd_sum, odd_squares_sum