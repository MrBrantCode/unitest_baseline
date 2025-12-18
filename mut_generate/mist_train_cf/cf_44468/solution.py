"""
QUESTION:
Estimate the minimum number of impressions required to achieve a 95% confidence interval of a specified width for the true click-through rate (CTR) of a new item in a recommender system. 

The confidence interval should have a maximum width of ε. Use the Wilson Score Interval method to estimate the interval width, which is approximately 2*1.96*sqrt(p*(1-p)/n), where p is the true CTR and n is the number of impressions. Assume the maximum possible width occurs at p = 0.5. The estimated number of impressions should ensure that the 95% confidence interval for the observed CTR includes the true CTR 95% of the time.
"""

import math

def min_impressions(epsilon):
    """
    Estimate the minimum number of impressions required to achieve a 95% confidence interval 
    of a specified width for the true click-through rate (CTR) of a new item in a recommender system.

    Args:
        epsilon (float): The maximum allowed width of the confidence interval.

    Returns:
        int: The estimated minimum number of impressions.
    """
    # The width of a 95% Wilson Score Interval is approximately 2*1.96*sqrt(p*(1-p)/n)
    # where p is the true click-through rate and n is the number of trials (or impressions in this case)
    # If we take the maximum value for width (which is at p = 0.5), and set it less than a certain pre-defined bound (say ε), 
    # we can solve for minimum n
    # 2*1.96*sqrt(0.5*(1-0.5)/n) < ε
    # This gives us:
    # n > (1.96/ε)^2 * (0.5*(1-0.5))

    return math.ceil((1.96 / epsilon) ** 2 * (0.5 * (1 - 0.5)))