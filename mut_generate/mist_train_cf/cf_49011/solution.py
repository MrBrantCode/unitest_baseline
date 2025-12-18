"""
QUESTION:
Combine the rankings of features from multiple machine learning algorithms into a final ranked list, taking into consideration the feature importance scores of the algorithms.
"""

def combine_rankings(rankings):
    """
    Combine the rankings of features from multiple machine learning algorithms into a final ranked list.
    
    Parameters:
    rankings (dict): A dictionary where keys are feature names and values are lists of importance scores from different algorithms.
    
    Returns:
    list: A list of tuples containing the feature name and its combined importance score.
    """
    
    # Initialize an empty dictionary to store the combined importance scores
    combined_importance = {}
    
    # Iterate over each feature and its importance scores
    for feature, scores in rankings.items():
        # Calculate the average importance score
        combined_importance[feature] = sum(scores) / len(scores)
    
    # Sort the features by their combined importance scores in descending order
    sorted_features = sorted(combined_importance.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_features