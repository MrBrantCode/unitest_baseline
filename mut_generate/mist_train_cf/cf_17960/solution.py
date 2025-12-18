"""
QUESTION:
Write a function `top_regions` that takes a list of dictionaries as input, where each dictionary contains 'name', 'region', and 'score' keys. The function should calculate the mean score for each region, excluding scores below 7, and return the top 5 regions with the highest mean score along with their corresponding mean scores. The function should not take any other parameters besides the input list.
"""

import numpy as np

def top_regions(array):
    """
    Calculate the mean score for each region, excluding scores below 7, 
    and return the top 5 regions with the highest mean score along with their corresponding mean scores.

    Parameters:
    array (list): A list of dictionaries containing 'name', 'region', and 'score' keys.

    Returns:
    dict: A dictionary with the top 5 regions as keys and their mean scores as values.
    """
    
    # Group the scores by region and exclude scores below 7
    grouped_scores = {}
    for entry in array:
        region = entry['region']
        score = entry['score']
        if score >= 7:
            if region in grouped_scores:
                grouped_scores[region].append(score)
            else:
                grouped_scores[region] = [score]

    # Calculate the mean for each region
    means = {}
    for region, scores in grouped_scores.items():
        mean_score = np.mean(scores)
        means[region] = mean_score

    # Sort the regions by mean score in descending order
    sorted_regions = sorted(means, key=means.get, reverse=True)

    # Get the top 5 regions with the highest mean score
    top_5_regions = {region: means[region] for region in sorted_regions[:5]}

    return top_5_regions