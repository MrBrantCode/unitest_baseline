"""
QUESTION:
Write a Python function named `calculate_data_skew` that takes a list of integers representing data sizes as input and returns the data skew, which is the difference between the maximum and minimum data sizes. The data skew should be calculated only when there are more than one node in the Hadoop cluster, i.e., the length of the data sizes list is greater than 1.
"""

def calculate_data_skew(data_sizes):
    """
    Calculate the data skew in a Hadoop cluster.

    The data skew is the difference between the maximum and minimum data sizes.
    It is only calculated when there are more than one node in the Hadoop cluster.

    Args:
        data_sizes (list): A list of integers representing data sizes.

    Returns:
        int: The data skew.
    """
    if len(data_sizes) > 1:
        return max(data_sizes) - min(data_sizes)
    else:
        return 0