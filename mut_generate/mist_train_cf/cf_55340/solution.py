"""
QUESTION:
Write a function named `reverse(x)` that takes a 32-bit signed integer `x` and returns its reversed digits as an integer, preserving the original sign. If the reversed integer exceeds the 32-bit signed integer range `[-2^31, 2^31 - 1]`, return `0` instead.
"""

def reverse(x):
    sign = [1,-1][x < 0]
    rst = sign*int(str(abs(x))[::-1])
    return rst if -(2**31)-1 < rst < 2**31 else 0