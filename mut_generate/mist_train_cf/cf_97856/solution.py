"""
QUESTION:
Write a function named `calculate_average_rating` that takes a list of ratings as input and returns the average rating, but only if at least one rating is above 3.5. If no ratings are above 3.5, return "No ratings above threshold". The function should utilize the NumPy library to efficiently handle large datasets.
"""

import numpy as np

def calculate_average_rating(ratings):
    ratings_above_threshold = np.array(ratings)[np.array(ratings) > 3.5]
    if len(ratings_above_threshold) > 0:
        return np.mean(ratings_above_threshold)
    else:
        return "No ratings above threshold"