"""
QUESTION:
Write a function `bitSwapRequired(a, b)` that calculates the number of bits that need to be flipped to convert integer `a` to integer `b`. The function takes two integers `a` and `b` as input and returns the number of bits that need to be flipped. Assume 32-bit integers.
"""

def bitSwapRequired(a: int, b: int) -> int:
    xor_result = a ^ b  
    count = 0
    while xor_result:
        count += xor_result & 1  
        xor_result >>= 1  
    return count