"""
QUESTION:
Given a dataset with N records where K records have both X and Y equal to 1, write a function called `hypergeometric_probability` to calculate the probability that in a random sample of size n, the number of records with X and Y equal to 1 is more than 50% of the sample size, without replacement. The function should take four parameters: N (total number of records), K (number of records with X and Y equal to 1), and n (sample size), and return the calculated probability.
"""

import math

def hypergeometric_probability(N, K, n):
    """
    Calculate the probability that in a random sample of size n from a population of size N, 
    the number of records with X and Y equal to 1 is more than 50% of the sample size, 
    given that K records in the population have both X and Y equal to 1.

    Args:
        N (int): The total number of records in the population.
        K (int): The number of records with X and Y equal to 1 in the population.
        n (int): The size of the random sample.

    Returns:
        float: The calculated probability.
    """

    # Calculate k0, the minimum number of records with X and Y equal to 1 in the sample
    k0 = math.ceil(n / 2)

    # Initialize the probability
    probability = 0.0

    # Calculate the probability for each possible number of records with X and Y equal to 1 in the sample
    for k in range(k0, min(n, K) + 1):
        # Calculate the combination of K items taken k at a time
        combination_K_k = math.comb(K, k)
        
        # Calculate the combination of (N-K) items taken (n-k) at a time
        combination_NK_nk = math.comb(N - K, n - k)
        
        # Calculate the combination of N items taken n at a time
        combination_N_n = math.comb(N, n)

        # Update the probability
        probability += (combination_K_k * combination_NK_nk) / combination_N_n

    return probability