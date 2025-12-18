"""
QUESTION:
Create a function `unique_binary_string` that takes three arguments: an integer `number`, an integer `lower_bound`, and an integer `upper_bound`. The function should return a unique binary string of length 32 based on the given decimal `number` within the range `[lower_bound, upper_bound]`. The binary string should take into account the number's position within the range, its factors, and the sum of its digits, and should be unique for each input number within the defined range.
"""

def unique_binary_string(number, lower_bound, upper_bound):
    position = (number - lower_bound) / (upper_bound - lower_bound)
    factors = [i for i in range(2, number+1) if number % i == 0]
    digits_sum = sum(int(digit) for digit in str(number))
    
    binary_string = format(int(position * 1000000) ^ int(''.join(str(f) for f in factors) + str(digits_sum)), 'b')
    
    return binary_string.zfill(32)  # Pad the string with zeroes to a fixed length