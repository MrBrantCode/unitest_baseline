"""
QUESTION:
Implement a function `calculate_probability(n, k, p)` that calculates the probability of an event occurring exactly `k` times out of `n` independent and identically distributed Bernoulli trials, where the probability of success for each trial is `p`. Use a recursive algorithm to calculate the binomial coefficient and do not use any built-in probability functions or libraries.
"""

def calculate_probability(n, k, p):
    """
    Calculate the probability of an event occurring exactly k times out of n independent and identically distributed Bernoulli trials,
    where the probability of success for each trial is p.

    Args:
    n (int): The total number of trials.
    k (int): The number of successes.
    p (float): The probability of success for each trial.

    Returns:
    float: The probability of getting exactly k successes.
    """

    def binomial_coefficient(a, b):
        if b == 0 or b == a:
            return 1
        else:
            return binomial_coefficient(a-1, b-1) + binomial_coefficient(a-1, b)

    binomial = binomial_coefficient(n, k)
    probability = binomial * (p ** k) * ((1 - p) ** (n - k))
    return probability