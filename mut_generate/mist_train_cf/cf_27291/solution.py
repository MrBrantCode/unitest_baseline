"""
QUESTION:
Write a function `countDigitOnes` that takes a positive integer `n` and returns the count of digit ones in its decimal representation. The input `n` is restricted to a positive integer where `1 <= n <= 10^9`.
"""

def countDigitOnes(n: int) -> int:
    count = 0
    for digit in str(n):
        if digit == '1':
            count += 1
    return count