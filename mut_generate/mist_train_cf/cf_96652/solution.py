"""
QUESTION:
Write a function named `count_combinations` that takes a string `string` and an integer `length` as input. The function should return the number of distinct combinations of `length` characters from the string, where each character can only be used once in each combination, and the result should be modulo 10^9+7. Assume the length of the string will not exceed 10^5 characters.
"""

MOD = int(1e9 + 7)

def count_combinations(string, length):
    unique_chars = set(string)
    n = len(unique_chars)
    r = length
    
    def factorial(x):
        result = 1
        for i in range(1, x+1):
            result = (result * i) % MOD
        return result

    def modular_inverse(a):
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            else:
                g, x, y = extended_gcd(b % a, a)
                return g, y - (b // a) * x, x

        g, x, _ = extended_gcd(a, MOD)
        if g == 1:
            return x % MOD

    numerator = factorial(n)
    denominator = (factorial(r) * factorial(n - r)) % MOD
    denominator_inverse = modular_inverse(denominator)
    return (numerator * denominator_inverse) % MOD