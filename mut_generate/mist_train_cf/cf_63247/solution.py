"""
QUESTION:
Create a function named `substring_n` that takes three arguments: `str_1`, `str_2`, and `n`, where `n` is a positive integer. The function should return a boolean indicating whether `str_1` appears at least `n` times as a substring in `str_2`.
"""

def substring_n(str_1, str_2, n):
    return str_2.count(str_1) >= n