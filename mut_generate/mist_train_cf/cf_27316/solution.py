"""
QUESTION:
Implement a function `check_binary_string` that takes a single parameter `binary_string` (1 <= len(binary_string) <= 10^5), a string representing a binary number, and returns `True` if the binary string consists of all zeroes or all ones, and `False` otherwise.
"""

def check_binary_string(binary_string):
    return set(binary_string) == {'0'} or set(binary_string) == {'1'}