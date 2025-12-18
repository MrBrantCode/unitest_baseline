"""
QUESTION:
Write a recursive function `reverse_integer(n)` that takes an integer `n` as input and returns the integer with its digits reversed. If the input integer is negative, the function should return the negative of the reversed integer. The function should not work with integers that have leading zeros and should assume the input is always an integer.
"""

def reverse_integer(n):
    if n < 0:  
        return -1 * reverse_integer(-n)
    elif n < 10:  
        return n
    else:  
        return int(str(n % 10) + str(reverse_integer(n // 10)))