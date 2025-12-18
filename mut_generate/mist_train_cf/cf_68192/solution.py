"""
QUESTION:
Given two integers `start` and `end` representing the range `[start, end]`, create a function `rangeBitwiseAnd` that returns the bitwise OR of all numbers in this range, inclusive. The function should take two parameters `start` and `end` and return an integer. The constraints for the function are `0 <= start <= end <= 2^31 - 1`.
"""

def rangeBitwiseAnd(start: int, end: int) -> int:
    shift = 0
    # find the common prefix
    while start < end:
        start >>= 1
        end >>= 1
        shift += 1
    return start << shift