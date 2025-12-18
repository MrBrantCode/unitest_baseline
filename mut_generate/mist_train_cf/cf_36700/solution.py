"""
QUESTION:
Write a function `reverse_integer(x)` that takes a 32-bit signed integer `x` as input and returns the reverse of the integer. If the reversed integer overflows, return 0. If the input integer is negative, return the reversed integer with a negative sign; otherwise, return the reversed integer.
"""

def reverse_integer(x: int) -> int:
    neg = x < 0
    if neg:
        x = -x
    reversed_int = 0
    while x != 0:
        pop = x % 10
        x = x // 10
        if reversed_int > (1 << 31) // 10 or (reversed_int == (1 << 31) // 10 and pop > 7):
            return 0
        if reversed_int < -(1 << 31) // 10 or (reversed_int == -(1 << 31) // 10 and pop < -8):
            return 0
        reversed_int = reversed_int * 10 + pop
    return -reversed_int if neg else reversed_int