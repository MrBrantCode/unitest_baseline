"""
QUESTION:
Write a function `findTrailingZeros(n)` that calculates the number of trailing zeros in the factorial of a given number `n`, where `n` can be up to 10^18. The function should be efficient in terms of time complexity, avoiding direct computation of the factorial due to its large size.
"""

def findTrailingZeros(n):
    count = 0
    i = 5
    while (n / i>= 1):
        count += int(n / i)
        i *= 5
    return int(count)