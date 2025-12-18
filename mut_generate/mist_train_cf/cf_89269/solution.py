"""
QUESTION:
Create a Python function named `append_zeros` that takes two parameters: `string` and `num_chars`. The function should append zeros to the end of the string until its length is equal to `num_chars`. The `num_chars` should be a prime number between 1000 and 10,000 (inclusive). The function should also validate if the `string` is a valid email address (i.e., it contains both "@" and "." characters). If `num_chars` is not within the specified range or is not a prime number, or if `string` is not a valid email address, the function should return an error message.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def append_zeros(string, num_chars):
    if num_chars < 1000 or num_chars > 10000:
        return "Invalid number of characters"

    if "@" not in string or "." not in string:
        return "Invalid email address"

    if not is_prime(num_chars):
        return "Invalid number of characters"

    return string + "0" * (num_chars - len(string))