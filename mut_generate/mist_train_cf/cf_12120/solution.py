"""
QUESTION:
Implement a function named `bayes_theorem` that calculates P(A | B) using Bayes' theorem with the given probabilities P(B | A), P(A), and P(B), without using any data structures to store intermediate results. The function should take P(B | A), P(A), and P(B) as input and return the calculated probability P(A | B).
"""

def bayes_theorem(P_B_given_A, P_A, P_B):
    """
    Calculate P(A | B) using Bayes' theorem.

    Parameters:
    P_B_given_A (float): Probability of B given A.
    P_A (float): Probability of A.
    P_B (float): Probability of B.

    Returns:
    float: The calculated probability P(A | B).
    """
    return (P_B_given_A * P_A) / P_B