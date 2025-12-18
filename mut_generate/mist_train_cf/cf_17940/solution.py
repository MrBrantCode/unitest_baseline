"""
QUESTION:
Write a function `binomialProb(n, p, k)` to calculate the probability of exactly `k` successes in `n` independent Bernoulli trials, each with a probability of success `p`, using a recursive algorithm. The function should take three parameters: `n` (the total number of trials), `p` (the probability of success in a single trial), and `k` (the number of successes).
"""

def binomialProb(n, p, k):
    """
    Calculate the probability of exactly k successes in n independent Bernoulli trials, 
    each with a probability of success p, using a recursive algorithm.

    Parameters:
    n (int): The total number of trials.
    p (float): The probability of success in a single trial.
    k (int): The number of successes.

    Returns:
    float: The probability of exactly k successes in n trials.
    """
    if k == 0 or k == n:
        return comb(n, k) * p**k * (1-p)**(n-k)
    else:
        return comb(n, k) * p**k * (1-p)**(n-k)

import math
def comb(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))