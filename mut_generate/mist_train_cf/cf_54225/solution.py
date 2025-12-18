"""
QUESTION:
Write a function `is_h0_rejected` that determines whether the null hypothesis (H0) is rejected in a two-sided test given a p-value from a right one-sided test and a significance level. The test is assumed to be symmetric, such as a Z-test or T-test with one population.

The function should take two parameters: `p_value_one_sided` and `significance_level`. The function should return `True` if H0 is rejected and `False` otherwise.
"""

def is_h0_rejected(p_value_one_sided, significance_level):
    """
    Determine whether the null hypothesis (H0) is rejected in a two-sided test given a p-value from a right one-sided test and a significance level.

    Parameters:
    p_value_one_sided (float): The p-value from a right one-sided test.
    significance_level (float): The significance level.

    Returns:
    bool: True if H0 is rejected, False otherwise.
    """
    # Since the test is symmetric, the two-sided p-value is twice the one-sided p-value
    p_value_two_sided = p_value_one_sided * 2
    
    # Reject H0 if the two-sided p-value is less than the significance level
    return p_value_two_sided < significance_level