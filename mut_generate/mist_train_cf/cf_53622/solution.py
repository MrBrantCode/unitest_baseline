"""
QUESTION:
Write a function `binomial_probability` that takes the number of trials `n`, the number of successes `k`, and the probability of success `p` as input and returns the probability of exactly `k` successes in `n` independent trials using the binomial probability formula. Then use this function to calculate the probability that a minimum of three out of five children are girls, assuming the probability of having a boy is equal to the probability of having a girl, i.e., `p = 0.5`.
"""

from math import comb

def binomial_probability(n, k, p):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))