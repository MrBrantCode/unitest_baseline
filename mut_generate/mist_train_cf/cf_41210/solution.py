"""
QUESTION:
Implement the `kl_dirichlet` function to calculate the Kullback-Leibler (KL) divergence between two sets of Dirichlet distributions `p` and `q`. The function should take two arrays of Dirichlet distribution parameters as input, where each element in the array corresponds to a different category. The function should return the KL divergence between the two sets of Dirichlet distributions. Ensure that the function handles arrays of different lengths by raising an assertion error if `p` and `q` do not have the same length.
"""

import numpy as np

def kl_dirichlet(p, q):
    # Ensure p and q have the same length
    assert len(p) == len(q), "Arrays p and q must have the same length"

    # Calculate the KL divergence for each pair of Dirichlet distributions
    kl_divergences = np.sum(p * (np.log(p) - np.log(q)), axis=0)

    return np.sum(kl_divergences)