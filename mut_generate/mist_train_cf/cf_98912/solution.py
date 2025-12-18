"""
QUESTION:
Given a binary string, write a function `transform_to_alternating_pattern` that transforms the binary string into an alternating pattern of 0's and 1's, ensuring the length of the pattern is a prime number. The function should return the transformed binary string if the length is prime, otherwise return an error message.
"""

import math

def transform_to_alternating_pattern(binary_string):
    binary_list = [int(bit) for bit in binary_string]
    pattern_length = len(binary_list)

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    if not is_prime(pattern_length):
        return "Pattern length is not a prime number"

    pattern = [0] * pattern_length
    for i in range(pattern_length):
        pattern[i] = i % 2

    transformed_binary_list = [str(pattern[i] * binary_list[i]) for i in range(pattern_length)]

    return ''.join(transformed_binary_list)