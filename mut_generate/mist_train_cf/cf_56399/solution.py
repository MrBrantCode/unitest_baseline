"""
QUESTION:
Write a function `simplifiedFractions(n)` that takes an integer `n` as input and returns a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to `n`, along with the count of fractions that have an odd numerator. The function should return the list of fractions as strings in the format "numerator/denominator" and the count of fractions with odd numerators. The input `n` is restricted to the range `1 <= n <= 100`.
"""

def simplifiedFractions(n):
    def gcd(a, b):
        if b == 0: return a
        return gcd(b, a % b)

    fractions = []
    odd_num = 0
    
    for den in range(2, n + 1):
        for num in range(1, den):
            if gcd(num, den) == 1:
                fractions.append(f'{num}/{den}')
                if num % 2 == 1:
                    odd_num += 1
                    
    return fractions, odd_num