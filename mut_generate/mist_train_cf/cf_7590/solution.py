"""
QUESTION:
Write a recursive function called `decimal_to_binary` that converts a positive integer `n` to its binary string representation. The function should handle the conversion recursively without any loops.
"""

def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)