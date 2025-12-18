"""
QUESTION:
Write a function `calculate_conditional_probability` that calculates the conditional probability of event A occurring, given event B has occurred, using Bayes' theorem, and checks for statistical independence between A and B. The function should take three arguments: `P_B_given_A` (the conditional probability of event B happening given event A), `P_A` (the individual probability of event A), and `P_B` (the particular probability of event B).
"""

def calculate_conditional_probability(P_B_given_A, P_A, P_B):
    """
    Calculate the conditional probability of event A occurring, given event B has occurred, 
    using Bayes' theorem, and check for statistical independence between A and B.

    Args:
        P_B_given_A (float): The conditional probability of event B happening given event A.
        P_A (float): The individual probability of event A.
        P_B (float): The particular probability of event B.

    Returns:
        float: The conditional probability of event A given event B.
    """
    P_A_given_B = (P_B_given_A * P_A) / P_B
    return P_A_given_B