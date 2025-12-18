"""
QUESTION:
Write a function `check_number(n)` that checks if a given number `n` is a power of three, finds the largest power of three that is less than or equal to `n`, and outputs the number of digits in the binary representation of the largest power of three. The function should handle numbers up to 10^9 and should be optimized for efficiency with a time complexity of O(log n).
"""

def check_number(n):
    if n <= 0:
        return False
    largest_power = 1
    while 3 * largest_power <= n:
        largest_power *= 3
    binary_digits = 0
    while largest_power != 0:
        binary_digits += 1
        largest_power >>= 1
    return binary_digits