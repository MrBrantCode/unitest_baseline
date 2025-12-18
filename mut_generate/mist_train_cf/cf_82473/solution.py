"""
QUESTION:
Write a function `compare_means` to compare two mean values from a one-way ANOVA test with a categorical variable of 3 levels. The function should determine which mean value is greater when one is positive and the other is negative. The function should consider the direction of the scale variable derived from factor analysis and return the result based on the actual values, not the interpretation of the factor.
"""

def compare_means(mean1, mean2):
    """
    Compare two mean values from a one-way ANOVA test and determine which mean value is greater.

    Args:
        mean1 (float): The first mean value.
        mean2 (float): The second mean value.

    Returns:
        str: The result of the comparison.
    """
    if mean1 > 0 and mean2 < 0:
        return "mean1 is greater"
    elif mean1 < 0 and mean2 > 0:
        return "mean2 is greater"
    else:
        if mean1 > mean2:
            return "mean1 is greater"
        elif mean1 < mean2:
            return "mean2 is greater"
        else:
            return "mean1 and mean2 are equal"