"""
QUESTION:
Write a function `calculate_power` that calculates the power of a given number `n` raised to the exponent `m`. The function should return an error message if `n` is negative and `m` is not an integer. If either `n` or `m` is greater than 1000, the function should use an efficient algorithm with a time complexity of O(log(m)) and a space complexity of O(1).
"""

from typing import Union

def calculate_power(n: int, m: int) -> Union[int, str]:
    # Handle edge cases
    if n < 0 and not isinstance(m, int):
        return "Error: Invalid input, m must be an integer"
    if n > 1000 or m > 1000:
        # Calculate power using more efficient algorithm
        binary_m = bin(m)[2:]
        result = 1
        power = n
        for bit in binary_m[::-1]:
            if bit == '1':
                result *= power
            power *= power
        return result
    else:
        # Calculate power using iterative or recursive algorithm
        result = 1
        for _ in range(m):
            result *= n
        return result