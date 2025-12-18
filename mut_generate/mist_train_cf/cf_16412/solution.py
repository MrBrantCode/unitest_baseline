"""
QUESTION:
Create a function called `int_to_binary` that takes a positive integer `n` as input and returns its binary representation as a string. The function should use a recursive approach and have a time complexity of O(log n).
"""

def int_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    elif n > 1:
        return int_to_binary(n // 2) + str(n % 2)