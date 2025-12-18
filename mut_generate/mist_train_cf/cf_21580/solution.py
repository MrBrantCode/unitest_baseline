"""
QUESTION:
Function `count_combinations(string, length)` 
Given a string and a length, find the number of distinct combinations of the given length from the characters in the string, considering each character can only be used once in each combination. The function should return the result modulo 10^9+7. The length of the string will not exceed 10^5 characters.
"""

MOD = int(1e9 + 7)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def modular_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g == 1:
        return x % m

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % MOD
    return result

def count_combinations(string, length):
    """
    Calculate the number of distinct combinations of a given length from the characters in a given string.

    Args:
    string (str): The input string.
    length (int): The length of combinations.

    Returns:
    int: The number of distinct combinations modulo 10^9+7.
    """
    unique_chars = set(string)
    n = len(unique_chars)
    r = length
    numerator = factorial(n)
    denominator = (factorial(r) * factorial(n - r)) % MOD
    denominator_inverse = modular_inverse(denominator, MOD)
    return (numerator * denominator_inverse) % MOD