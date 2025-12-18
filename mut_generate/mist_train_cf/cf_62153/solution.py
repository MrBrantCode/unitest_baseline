"""
QUESTION:
Implement a function `calculate_bayesian_credible_interval` to compute Bayesian Credible Intervals from an MCMC chain. The function should take as input a list of samples from the posterior distribution and the desired level of confidence (between 0 and 1), and return the lower and upper bounds of the credible interval. The function should sort the samples in ascending order, discard the samples at the lower and upper ends of the distribution according to the desired level of confidence, and return the remaining samples as the credible interval.
"""

def calculate_bayesian_credible_interval(samples, confidence):
    sorted_samples = sorted(samples)
    ci_index = int((1 - confidence) / 2 * len(sorted_samples))
    lower_bound = sorted_samples[ci_index]
    upper_bound = sorted_samples[-ci_index - 1]
    return lower_bound, upper_bound