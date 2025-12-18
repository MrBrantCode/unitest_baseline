"""
QUESTION:
Create a function named `sum_within_bounds_and_average` that takes an integer list `l`, two integers `lower_bound` and `upper_bound`, and a float `min_average` as parameters. The function should return `True` if the sum of all elements in `l` falls within the range of `lower_bound` and `upper_bound` (inclusive) and if the average of the elements in `l` exceeds `min_average`. If either condition is not met, the function should return `False`. The function should also handle the case where the input list `l` is empty.
"""

def sum_within_bounds_and_average(l, lower_bound, upper_bound, min_average):
    """
    Checks if the sum of elements in a list falls within a specified range and 
    if the average exceeds a minimum average.

    Args:
        l (list): A list of integers.
        lower_bound (int): The lower bound of the range (inclusive).
        upper_bound (int): The upper bound of the range (inclusive).
        min_average (float): The minimum average required.

    Returns:
        bool: True if the sum is within the range and the average exceeds the minimum, False otherwise.
    """

    # Checking if the list is not empty to avoid division by zero error
    if len(l) == 0:
        return False

    total = sum(l)
    average = total / len(l)

    # Checking if the total is within the bounds and average is greater than min_average
    return lower_bound <= total <= upper_bound and average > min_average