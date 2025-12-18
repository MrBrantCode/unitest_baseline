"""
QUESTION:
Write a function `is_narcissistic_number` that determines if a given integer is a Narcissistic number or not. A Narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits. The input integer will always be within the range of 1 to 10^9. The function should return True if the input integer is a Narcissistic number, False otherwise.
"""

def is_narcissistic_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    total_sum = 0
    
    for digit in num_str:
        total_sum += int(digit) ** num_digits
    
    return total_sum == num