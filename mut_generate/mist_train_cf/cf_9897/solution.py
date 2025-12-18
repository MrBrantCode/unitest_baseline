"""
QUESTION:
Create a function called `decimal_to_binary` that converts a given positive integer into its binary representation using a recursive approach. The function should have a time complexity of O(log n), where n is the given integer.
"""

def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)