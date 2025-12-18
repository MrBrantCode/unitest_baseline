"""
QUESTION:
Create a function called `check_normality_proportions` that takes as input the sample sizes and proportions of two groups (n1, p1, n2, p2). The function should return True if the normality condition is met for the two-sample z-test for proportions, and False otherwise. The normality condition is met if n1p1, n1(1-p1), n2p2, and n2(1-p2) are all greater than or equal to 5.
"""

def check_normality_proportions(n1, p1, n2, p2):
    """
    Checks if the normality condition is met for the two-sample z-test for proportions.

    Args:
        n1 (int): Sample size of group 1.
        p1 (float): Proportion of group 1.
        n2 (int): Sample size of group 2.
        p2 (float): Proportion of group 2.

    Returns:
        bool: True if the normality condition is met, False otherwise.
    """
    return (n1 * p1 >= 5 and n1 * (1 - p1) >= 5 and 
            n2 * p2 >= 5 and n2 * (1 - p2) >= 5)