"""
QUESTION:
Compute the mean age of a cohort given a list of ages. Create a function called `compute_mean_age` that takes a list of integers representing the ages of individuals in a cohort and returns the mean age as a float. The input list will contain only non-negative integers and will have at least one element.
"""

def compute_mean_age(ages):
    """
    Compute the mean age of a cohort given a list of ages.

    Args:
        ages (list): A list of integers representing the ages of individuals in a cohort.

    Returns:
        float: The mean age of the cohort.
    """
    return sum(ages) / len(ages)