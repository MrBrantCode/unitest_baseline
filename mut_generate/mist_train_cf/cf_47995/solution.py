"""
QUESTION:
Given an alphabet Σ of α symbols, compute the count of incomplete words over Σ that do not exceed n in length, denoted as I(α,n), and return the result in modulo 1,000,000,007. Implement a function `incomplete_words(alpha, n)` that takes two parameters: `alpha` (the number of symbols in the alphabet) and `n` (the maximum length of the words), and returns I(α,n) modulo 1,000,000,007.
"""

def powerMod(base, exponent, mod):
    """Exponentiation by squaring and modulo"""
    if exponent == 0:
        return 1
    else:
        p = powerMod(base, exponent//2, mod)
        p = (p * p) % mod
        if exponent % 2 != 0:
            p = (p * base) % mod
        return p


def incomplete_words(alpha, n):
    """
    Compute the count of incomplete words over Σ that do not exceed n in length.

    Parameters:
    alpha (int): The number of symbols in the alphabet.
    n (int): The maximum length of the words.

    Returns:
    int: The count of incomplete words modulo 1,000,000,007.
    """
    mod = 10**9 + 7
    alphaFact = 1

    # Calculate alpha!
    for i in range(2, alpha + 1):
        alphaFact = (alphaFact * i) % mod

    # Calculate alpha^n and alpha!
    totalSeq = powerMod(alpha, n, mod)

    # Return I(α,n) modulo 1,000,000,007
    return (totalSeq - alphaFact) % mod