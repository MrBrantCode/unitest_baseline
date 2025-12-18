"""
QUESTION:
Write a function `addBinary` that takes two non-empty binary strings `a` and `b` as input, each containing only characters 1 or 0, and returns their sum as a binary string. The function should handle binary addition, including carrying over when the sum of two digits exceeds 1.
"""

def addBinary(a, b):
    result = ""
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        result = str(carry % 2) + result
        carry //= 2
    return result