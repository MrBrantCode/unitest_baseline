"""
QUESTION:
Given a Poisson process with rate λ, write a function `poisson_probability` that calculates the probability P(N(s) = k|N(t) = n) for s > t and s < t. Consider the memoryless property of the Poisson process, which affects the independence of events when s > t.
"""

from math import exp

def poisson_probability(rate, s, t, k, n):
    """
    Calculate the probability P(N(s) = k|N(t) = n) for a Poisson process.

    Parameters:
    rate (float): The rate of the Poisson process.
    s (float): The time at which the event occurs.
    t (float): The time at which the condition is given.
    k (int): The number of events at time s.
    n (int): The number of events at time t.

    Returns:
    float: The probability P(N(s) = k|N(t) = n).
    """

    # If s > t, the events are independent due to the memoryless property of the Poisson process.
    if s > t:
        # Calculate the probability using the Poisson distribution formula.
        probability = (exp(-rate * (s - t)) * (rate * (s - t)) ** (k - n)) / math.factorial(k - n) if k >= n else 0
        return probability
    # If s < t, the probability depends on the number of events at time t.
    elif s < t:
        # Calculate the probability using the Poisson distribution formula and the condition.
        probability = (exp(-rate * s) * (rate * s) ** k) / math.factorial(k) if n >= k else 0
        return probability
    else:
        # If s == t, the events are the same, so the probability is 1 if k == n, 0 otherwise.
        return 1 if k == n else 0