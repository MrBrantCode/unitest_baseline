"""
QUESTION:
Write a function `digitSum(n, b)` that calculates the sum of the digits of a given positive integer `n` in a specific base `b` (2 ≤ `b` ≤ 10) and returns the sum also represented in base `b`.
"""

def digitSum(n, b):
    def toBase(num, base):
        convertString = "0123456789ABCDEF"
        if num < base:
            return convertString[num]
        else:
            return toBase(num//base, base) + convertString[num%base]

    num_sum = sum(int(digit)  for digit in str(n))
    return toBase(num_sum, b)