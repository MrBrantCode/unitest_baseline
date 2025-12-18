"""
QUESTION:
Given an integer `n`, write a function `isPowerOfThree` that returns `true` if it is a power of three and `false` otherwise. A power of three is a number that can be expressed as `3^x` for some integer `x`. Do not use any built-in math functions or operators (`pow`, `log`, `*`, `/`, `sqrt`, etc.) in the solution. The function should work within the range `-2^31 <= n <= 2^31 - 1`.
"""

def isPowerOfThree(n: int) -> bool:
    powersOfThree = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323,
    4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
    return n in powersOfThree