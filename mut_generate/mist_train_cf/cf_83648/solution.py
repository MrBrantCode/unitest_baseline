"""
QUESTION:
Write a function `f(n)` that calculates the number of words of length `n` that can be constructed using the letters `A`, `E`, `F`, and `R` such that each of the four keywords "FREE", "FARE", "AREA", and "REEF" appears exactly once in the word. The function should return 0 if `n` is not a multiple of 4.
"""

def f(n):
    if n % 4:
        return 0
    n //= 4
    fact = [1]
    for i in range(1, n+1):
        fact.append(fact[-1]*i)
    res = 0
    for i in range(1, n):
        for j in range(1, n-i+1):
            k = n-i-j
            res += fact[n]*64*fact[n-1]//(fact[i]*fact[j]*fact[k])
    return res * 4