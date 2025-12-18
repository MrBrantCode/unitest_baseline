"""
QUESTION:
Create a function called `top_regions` that takes a list of dictionaries as input where each dictionary contains 'name', 'region', and 'score' keys. The function should group the input data by the 'region' key, exclude scores below 8, calculate the mean score for each region, and return the top 10 regions with the highest mean score.
"""

import numpy as np

def top_regions(array):
    """
    This function takes a list of dictionaries as input where each dictionary contains 'name', 'region', and 'score' keys.
    It groups the input data by the 'region' key, excludes scores below 8, calculates the mean score for each region, 
    and returns the top 10 regions with the highest mean score.

    Args:
        array (list): A list of dictionaries containing 'name', 'region', and 'score' keys.

    Returns:
        list: The top 10 regions with the highest mean score.
    """

    # Group the array by 'region' key
    grouped = {}
    for item in array:
        region = item['region']
        score = item['score']
        if region not in grouped:
            grouped[region] = []
        grouped[region].append(score)

    # Calculate the mean for each group and exclude scores below 8
    means = {}
    for region, scores in grouped.items():
        scores_above_8 = [score for score in scores if score >= 8]
        if scores_above_8:
            mean = np.mean(scores_above_8)
            means[region] = mean

    # Sort the regions by mean score in descending order
    sorted_regions = sorted(means.items(), key=lambda x: x[1], reverse=True)

    # Get the top 10 regions with the highest mean score
    top_10_regions = sorted_regions[:10]

    return top_10_regions