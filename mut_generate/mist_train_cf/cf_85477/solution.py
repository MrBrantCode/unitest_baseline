"""
QUESTION:
Write a function f(n) that calculates the number of ways to arrange 12n musicians into 4n trios, ensuring that no musician is paired with a former quartet partner from the previous day's 3n quartets. The function should return the result modulo 1,000,000,007.
"""

def f(n):
    MOD = 1000000007
    result = 1
    
    for i in range(1, 12 * n + 1):
        if i % 3 == 0:
            result = (result * (i // 3)) % MOD
        else:
            result = (result * i) % MOD
    
    denominator = 1
    for i in range(1, 4 * n + 1):
        denominator = (denominator * (i // 3)) % MOD if i % 3 == 0 else denominator
    
    return (result * pow(denominator, MOD - 2, MOD)) % MOD