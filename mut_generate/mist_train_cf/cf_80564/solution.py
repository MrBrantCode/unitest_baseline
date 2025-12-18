"""
QUESTION:
Write a function `int_to_base_neg2(N)` that converts a given integer `N` to a string in base -2, composed of '0's and '1's, without leading zeroes (unless the string is "0"). The function should handle all numbers within the range `0 <= N <= 10^9`.
"""

def int_to_base_neg2(N: int) -> str:
    if N == 0:
        return "0"
    res = []
    while N != 0:
        quotient, remainder = divmod(N, -2)
        if remainder < 0:
            quotient, remainder = quotient + 1, remainder + 2
        res.append(str(remainder))
        N = quotient
    return "".join(res[::-1])