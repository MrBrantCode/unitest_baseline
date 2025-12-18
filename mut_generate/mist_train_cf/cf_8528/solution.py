"""
QUESTION:
Implement a function named lucas_number(n) that uses a recursive approach to calculate the nth Lucas number. The function should be able to handle any non-negative integer input n, where the Lucas sequence is defined such that lucas_number(0) returns 2 and lucas_number(1) returns 1, and for any n greater than 1, the function returns the sum of the two preceding Lucas numbers, lucas_number(n-1) and lucas_number(n-2).
"""

def lucas_number(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_number(n - 1) + lucas_number(n - 2)