"""
QUESTION:
Write a function named `get_armstrong_numbers` that takes two integer parameters `lower` and `upper` representing a range of numbers. The function should return a list of all Armstrong numbers within the given range, inclusive, in ascending order. If the range is invalid (lower bound is not less than or equal to the upper bound) or contains more than 100 numbers, return an error message.
"""

def get_armstrong_numbers(lower, upper):
    if not isinstance(lower, int) or not isinstance(upper, int):
        return "Error: Range limits must be integers."
    
    if lower > upper:
        return "Error: Lower bound must be less than or equal to the upper bound."
    
    if upper - lower + 1 > 100:
        return "Error: Range contains more than 100 numbers."
    
    def is_armstrong_number(num):
        num_str = str(num)
        num_digits = len(num_str)
        sum = 0
        for digit in num_str:
            sum += int(digit) ** num_digits
        return sum == num
    
    armstrong_numbers = [num for num in range(lower, upper+1) if is_armstrong_number(num)]
    return armstrong_numbers