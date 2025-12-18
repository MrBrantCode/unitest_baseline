"""
QUESTION:
Write a function `bayes_theorem` that calculates the posterior probability P(D | TP) using Bayes' theorem. The function takes four parameters: the prior probability of having the disease `p_d`, the probability of testing positive when the disease is present `p_tp_given_d`, the probability of testing negative when the disease is not present `p_tn_given_not_d`. The function returns the posterior probability of having the disease given a positive test result.
"""

def bayes_theorem(p_d, p_tp_given_d, p_tn_given_not_d):
    """
    Calculate the posterior probability P(D | TP) using Bayes' theorem.

    Parameters:
    p_d (float): The prior probability of having the disease.
    p_tp_given_d (float): The probability of testing positive when the disease is present.
    p_tn_given_not_d (float): The probability of testing negative when the disease is not present.

    Returns:
    float: The posterior probability of having the disease given a positive test result.
    """
    # Calculate the probability of a positive test given that the disease is not present
    p_tp_given_not_d = 1 - p_tn_given_not_d
    
    # Calculate the probability of not having the disease
    p_not_d = 1 - p_d
    
    # Calculate the probability of a positive test
    p_tp = (p_tp_given_d * p_d) + (p_tp_given_not_d * p_not_d)
    
    # Calculate the posterior probability using Bayes' theorem
    p_d_given_tp = (p_tp_given_d * p_d) / p_tp
    
    return p_d_given_tp