"""
QUESTION:
Create a function `check_number(n)` that checks if a given positive integer `n` is a power of three. If it is, find the largest power of three that is less than or equal to `n`. The function should also calculate the number of digits in the binary representation of the largest power of three. The function should be able to handle numbers up to 10^9 and should have a time complexity of O(log n).
"""

def check_number(n):
    if n <= 0:
        return False
    power = 1
    while 3 ** power <= n:
        power += 1
    largest_power_of_three = 3 ** (power - 1)
    num_binary_digits = len(bin(largest_power_of_three)[2:])
    return is_power_of_three(n), largest_power_of_three, num_binary_digits

def is_power_of_three(n):
    while n % 3 == 0:
        n //= 3
    return n == 1