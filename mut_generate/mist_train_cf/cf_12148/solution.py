"""
QUESTION:
Implement the `content_based_filtering` function that takes the user's preferences vector `user_preferences`, the item dataset `item_dataset`, the weight vector for features `feature_weights`, and the list of item IDs already rated by the user `rated_items`. 

The function should calculate the weighted cosine similarity between the user's preferences vector and each item in the dataset, then return the top 3 item IDs with the highest similarity scores, excluding any items that the user has already rated. The `user_preferences`, `item_dataset`, `feature_weights`, and `rated_items` variables are represented as numpy arrays or dictionaries as shown in the provided code snippet.
"""

import numpy as np

def content_based_filtering(user_preferences, item_dataset, feature_weights, rated_items):
    similarities = {}
    for item_id, item_vector in item_dataset.items():
        weighted_vector = item_vector * feature_weights
        similarity = np.dot(user_preferences, weighted_vector) / (
                np.linalg.norm(user_preferences) * np.linalg.norm(weighted_vector)
        )
        similarities[item_id] = similarity

    sorted_items = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    recommended_items = [item_id for item_id, similarity in sorted_items if item_id not in rated_items]
    
    return recommended_items[:3]