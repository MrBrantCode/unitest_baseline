"""
QUESTION:
Implement a function called `binomialCoefficient(n, k)` where `n` is a positive integer greater than or equal to `k`. The function should return the binomial coefficient of `n` and `k` modulo 10^9+7.
"""

def binomialCoefficient(n, k):
    # Base cases
    if k == 0 or k == n:
        return 1
    
    # Compute factorials using dynamic programming
    factorials = [1] * (n+1)
    for i in range(2, n+1):
        factorials[i] = (factorials[i-1] * i) % (10**9 + 7)
    
    # Compute binomial coefficient using factorials and modular inverse
    coefficient = (factorials[n] * pow(factorials[k], 10**9 + 7 - 2, 10**9 + 7) * pow(factorials[n-k], 10**9 + 7 - 2, 10**9 + 7)) % (10**9 + 7)
    
    return coefficient