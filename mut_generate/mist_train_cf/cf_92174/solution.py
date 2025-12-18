"""
QUESTION:
Implement a function named `content_based_filtering` that takes in four parameters: `user_preferences`, `item_dataset`, `feature_weights`, and `rated_items`. `user_preferences` is a vector representing the user's preferences, `item_dataset` is a dictionary where the keys are item IDs and the values are vectors describing the characteristics of each item, `feature_weights` is a vector representing the weights assigned to different features, and `rated_items` is a list of item IDs that the user has already rated. The function should use a weighted cosine similarity algorithm to recommend the top 3 items that closely align with the user's preferences, excluding any items that the user has already rated.
"""

import numpy as np

def content_based_filtering(user_preferences, item_dataset, feature_weights, rated_items):
    # Calculate weighted cosine similarity
    similarities = {}
    for item_id, item_vector in item_dataset.items():
        weighted_vector = item_vector * feature_weights
        similarity = np.dot(user_preferences, weighted_vector) / (
                np.linalg.norm(user_preferences) * np.linalg.norm(weighted_vector)
        )
        similarities[item_id] = similarity

    # Sort items based on similarity scores
    sorted_items = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    # Filter out items already rated by the user
    recommended_items = [item_id for item_id, similarity in sorted_items if item_id not in rated_items]

    # Return top 3 recommendations
    return recommended_items[:3]