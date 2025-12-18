"""
QUESTION:
Create a recursive function called `reverse_num` that takes an integer `n` as input and returns the integer with its digits reversed. The function should handle integers of any length and not treat them as strings. If the input integer has trailing zeros, the output will not have those zeros.
"""

def reverse_num(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10 ** len(str(n // 10)) + reverse_num(n // 10)