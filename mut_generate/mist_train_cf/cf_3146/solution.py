"""
QUESTION:
Calculate the top 10 regions with the highest mean score by grouping a list of dictionaries by the 'region' key, excluding scores below 8, and sorting the regions by mean score in descending order. 

The input list contains dictionaries with 'name', 'region', and 'score' keys. The function should take this list as input and return the top 10 regions with their corresponding mean scores.
"""

import numpy as np

def top_regions_by_mean_score(regions):
    # Group the array by 'region' key
    grouped = {}
    for item in regions:
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
    return sorted_regions[:10]