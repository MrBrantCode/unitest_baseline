"""
QUESTION:
Implement the function `russian_peasant_multiplication` that multiplies two given positive integers `a` and `b` without using the multiplication operator. The function should have a time complexity of less than O(n) and a space complexity of less than O(log n), where n is the larger number.
"""

def russian_peasant_multiplication(a, b):
    result = 0

    while a > 0:
        if a % 2 == 1:  # if a is odd
            result += b

        a = a // 2  # halve a
        b = b * 2  # double b

    return result