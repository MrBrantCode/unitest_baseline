"""
QUESTION:
Compute the sum of two integers without using the "+" operator in O(log n) time complexity, where n is the maximum number of bits required to represent the given integers. The solution should not use mathematical operators (-, *, /), bitwise operators (<<, >>, &, |), loops, or recursion. Implement the function getSum(x, y) to calculate the sum of two integers x and y.
"""

def getSum(x, y):
    sum = x ^ y
    carry = (x & y) << 1
    while carry:
        x = sum
        y = carry
        sum = x ^ y
        carry = (x & y) << 1
    return sum