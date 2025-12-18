"""
QUESTION:
Develop a Python function named `append_zeros` that takes two parameters: `string` and `num_chars`. This function should append zeros to the end of the `string` until its length is equal to `num_chars`, but only if `num_chars` is a prime number and `string` is a valid email address. The function should return an error message if `num_chars` is less than 2, if `string` is not a valid email address, or if `num_chars` is not a prime number.
"""

import re

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def append_zeros(string, num_chars):
    if num_chars < 2:
        return "Invalid input"

    if not re.match(r"[^@]+@[^@]+\.[^@]+", string):
        return "Invalid email address"

    if not is_prime(num_chars):
        return "Invalid number of characters"

    return string + "0" * (num_chars - len(string))