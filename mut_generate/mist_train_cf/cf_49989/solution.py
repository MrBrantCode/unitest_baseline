"""
QUESTION:
Write a function `quick_power(base, n)` that calculates the power of a number modulo 1,000,000,007 using the fast exponentiation algorithm. Then use this function to compute `(3^(2^25) - 2^(2^25)) % 1,000,000,007 - 1`, where `pow` is 1,000,000,007. The function `quick_power(base, n)` should take two parameters: `base` and `n`, and return the result of `base` raised to the power of `n` modulo `pow`. The result should be the position of the first unpredictable permutation in the lexicographic list for `N = 2^25`.
"""

pow = 1000000007 

def quick_power(base, n):
    result = 1
    while n:
        if n & 1:
            result = (result * base) % pow
        base = (base * base) % pow
        n >>= 1
    return result