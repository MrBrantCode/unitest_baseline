"""
QUESTION:
Implement a function `russian_peasant_multiplication(a, b)` that multiplies two positive integers `a` and `b` without using the multiplication operator. The time complexity should be O(log n) and the space complexity should be O(log n), where n is the larger number.
"""

def russian_peasant_multiplication(a, b):
    result = 0

    while a > 0:
        if a % 2 == 1:  # if a is odd
            result += b

        a = a // 2  # halve a
        b = b * 2  # double b

    return result