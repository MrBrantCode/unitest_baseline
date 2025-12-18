"""
QUESTION:
Write a recursive function `reverse_number(n, rev=0)` that reverses the digits of a given non-negative integer `n`. The function should handle recursion efficiently and return the reversed number.
"""

def entance(n, rev=0):
    # Base case: if the number is 0, return the reversed number
    if n == 0:
        return rev
    # Recursive case: append the last digit of n to rev and recursively call
    # the function with n without the last digit and the new rev
    else:
        return entance(n // 10, rev * 10 + n % 10)