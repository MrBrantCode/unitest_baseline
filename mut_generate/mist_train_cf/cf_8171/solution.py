"""
QUESTION:
Write a function named `add_without_operator(a, b)` that takes two positive integers less than 100 as input, where both integers are prime numbers. The function should return the sum of the two integers without using the addition operator or any mathematical operators. The time complexity should be O(n), where n is the sum of the two input numbers.
"""

def add_without_operator(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a