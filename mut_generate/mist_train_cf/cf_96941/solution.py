"""
QUESTION:
Write a recursive function named `number_to_string(num)` that converts an integer `num` to its string representation. The function should handle both positive and negative integers.
"""

def number_to_string(num):
    if num < 0:
        return '-' + number_to_string(-num)
    elif num < 10:
        return str(num)
    else:
        return number_to_string(num // 10) + str(num % 10)