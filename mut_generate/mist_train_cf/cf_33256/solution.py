"""
QUESTION:
Implement a function `calculate_KL_divergence` that calculates the difference between the Kullback-Leibler (KL) divergence of two pairs of probability distributions. 

The function should take the means and variances of the prior and posterior distributions for two objects i and j as input parameters. It should return the difference between the KL divergence of object j and object i.

The input parameters are: 
- `mu_prior_i` and `var_prior_i`: the mean and variance of the prior distribution for object i
- `mu_posterior_i` and `var_posterior_i`: the mean and variance of the posterior distribution for object i
- `mu_prior_j` and `var_prior_j`: the mean and variance of the prior distribution for object j
- `mu_posterior_j` and `var_posterior_j`: the mean and variance of the posterior distribution for object j

The function should return a float value representing the difference between the KL divergence of object j and object i. 

The KL divergence is calculated using the formula: 
KL = 0.5 * (log(var_posterior / var_prior) + (var_prior + (mu_prior - mu_posterior)^2) / var_posterior - 1)
"""

import math

def calculate_KL_divergence(mu_prior_i: float, var_prior_i: float, mu_posterior_i: float, var_posterior_i: float, mu_prior_j: float, var_prior_j: float, mu_posterior_j: float, var_posterior_j: float) -> float:
    kl_divergence_i = 0.5 * (math.log(var_posterior_i / var_prior_i) + (var_prior_i + (mu_prior_i - mu_posterior_i)**2) / var_posterior_i - 1)
    kl_divergence_j = 0.5 * (math.log(var_posterior_j / var_prior_j) + (var_prior_j + (mu_prior_j - mu_posterior_j)**2) / var_posterior_j - 1)
    return kl_divergence_j - kl_divergence_i