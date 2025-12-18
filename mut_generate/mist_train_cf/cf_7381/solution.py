"""
QUESTION:
Write a function `reverse_and_sum_digits(x)` that takes a 32-bit signed integer `x` as input, reverses the integer while preserving its sign, and returns the sum of its digits. If the reversed integer overflows, return 0. The function should have a time complexity of O(logN) and a space complexity of O(1), where N is the absolute value of the input integer. The input integer will be within the range [-2^31, 2^31 - 1] and will not have leading zeros. Use bitwise operations and arithmetic operations to solve the problem.
"""

def reverse_and_sum_digits(x):
    reversed_num = 0
    digit_sum = 0
    is_negative = False
    
    if x < 0:
        is_negative = True
    
    x = abs(x)
    
    while x > 0:
        reversed_num = (reversed_num * 10) | (x % 10)
        digit_sum += x % 10
        x //= 10
    
    if is_negative:
        reversed_num *= -1
    
    if reversed_num > 2**31 - 1 or reversed_num < -2**31:
        return 0
    
    return digit_sum