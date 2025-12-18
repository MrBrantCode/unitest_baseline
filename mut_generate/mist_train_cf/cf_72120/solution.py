"""
QUESTION:
Given a numerical value `n`, write a function `is_unattractive(n: int) -> bool` to return a boolean value indicating whether `n` is an unattractive number. An unattractive number is a positive integer whose prime factors are exclusively `2`, `3`, and/or `5`. The function should handle integers in the range `-2^31 <= n <= 2^31 - 1`.
"""

def is_unattractive(n: int) -> bool:
    if n <= 0:
        return False
    for i in [2, 3, 5]:
        while n % i == 0:
            n /= i
    return n == 1