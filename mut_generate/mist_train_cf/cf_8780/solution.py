"""
QUESTION:
Write a function named `findLargest` that takes two non-negative integers `a` and `b` as input and returns the largest number without using any arithmetic operators (+, -, *, /, %). The function should only use bitwise operators and logical operators, and it should run in O(1) time complexity and use O(1) space complexity.
"""

def findLargest(a, b):
    result = 0

    for i in range(31, -1, -1):
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1

        if bit_a == 1 and bit_b == 0:
            result = a
            break
        elif bit_a == 0 and bit_b == 1:
            result = b
            break

    return result