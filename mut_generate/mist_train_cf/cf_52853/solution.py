"""
QUESTION:
Write a function named 'max_unique_instances' that takes as input a list of integers representing the number of potential values for each discrete attribute and returns the maximum number of unique instances that can be produced by these attributes. Assume the function does not take into account the classification category, as it does not affect the number of unique instances.
"""

def max_unique_instances(attributes):
    """
    Calculate the maximum number of unique instances that can be produced by discrete attributes.

    Args:
    attributes (list): A list of integers representing the number of potential values for each discrete attribute.

    Returns:
    int: The maximum number of unique instances.
    """
    max_instances = 1
    for attribute in attributes:
        max_instances *= attribute
    return max_instances