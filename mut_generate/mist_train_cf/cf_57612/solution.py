"""
QUESTION:
Write a function `performance_criterion_ratio` that takes an even integer `n` greater than 2 as input and returns the ratio of the performance criterion of a fully interconnected network to that of a ring network.

The performance criterion is the product of the required number of links for the network and the worst-case path length spanning any pair of two processors. 

Note that the function should not take any other inputs and should not output or print anything other than the ratio.
"""

def performance_criterion_ratio(n):
    """
    Calculate the ratio of the performance criterion of a fully interconnected network to that of a ring network.

    Args:
        n (int): An even integer greater than 2.

    Returns:
        float: The ratio of the performance criterion of a fully interconnected network to that of a ring network.
    """
    return (n - 1) / n