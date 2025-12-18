"""
QUESTION:
Implement the "average_precision" function to calculate the average precision for a given set of search results and a specified cutoff. The function should take two parameters: "results" (a list of result objects, where each result object has an "is_relevant" attribute indicating whether the result is relevant) and "cutoff" (the specified cutoff for calculating the average precision). The function should return the average precision for the given set of search results up to the specified cutoff.
"""

import numpy as np

def average_precision(results, cutoff):
    """
    Calculate the average precision for a given set of search results and a specified cutoff.

    Parameters:
    results (list): A list of result objects, where each result object has an "is_relevant" attribute.
    cutoff (int): The specified cutoff for calculating the average precision.

    Returns:
    float: The average precision for the given set of search results up to the specified cutoff.
    """
    relevant_count = 0
    precision_sum = 0.0
    for i, result in enumerate(results[:cutoff]):  # Apply the cutoff
        if result.is_relevant:  
            relevant_count += 1
            precision_sum += relevant_count / (i + 1)
    if relevant_count == 0:
        return 0.0
    return precision_sum / relevant_count