"""
QUESTION:
Create a function `unique_binary_string(number, lower_bound, upper_bound)` that generates a unique binary string of length 32 for a given decimal number within a specific range defined by `lower_bound` and `upper_bound`. The binary string should not match any other output for any input within the defined range.
"""

def unique_binary_string(number, lower_bound, upper_bound):
    position = (number - lower_bound) / (upper_bound - lower_bound)
    factors = [i for i in range(2, number+1) if number % i == 0]
    digits_sum = sum(int(digit) for digit in str(number))
    binary_string = format(int(position * 1000000) ^ int(''.join(str(f) for f in factors) + str(digits_sum)), 'b')
    return binary_string.zfill(32)