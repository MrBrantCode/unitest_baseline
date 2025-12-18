"""
QUESTION:
Implement a function `estimate_integral` to estimate the integral of a given function `g(x)` under a Gamma distribution using Monte Carlo integration with samples obtained from the Gamma distribution via accept-reject sampling. The function should take in the samples from the Gamma distribution and the function `g(x)` as inputs, and return the estimated integral value.
"""

def estimate_integral(g, samples):
    """
    Estimates the integral of a given function g(x) under a Gamma distribution 
    using Monte Carlo integration with samples obtained from the Gamma distribution.

    Args:
    g (function): The function to be integrated.
    samples (list): Samples from the Gamma distribution.

    Returns:
    float: The estimated integral value.
    """
    return sum(g(sample) for sample in samples) / len(samples)