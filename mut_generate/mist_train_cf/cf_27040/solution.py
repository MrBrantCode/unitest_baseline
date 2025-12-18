"""
QUESTION:
Implement the `process_location_data` function, which takes in `location_features_dict`, `labels`, `lead_days`, and `days_window` as inputs, and returns a dictionary containing processed features and labels for each location. The function must perform the following steps: 

- Sort the common locations in ascending order.
- For each common location: 
  - Retrieve feature vectors (X) and corresponding labels (y) from the input dictionaries.
  - Convert X and y into NumPy arrays.
  - Eliminate the last `lead_days + days_window` days from X to match the shape of the labels array.

The function signature should be `def process_location_data(location_features_dict: dict, labels: dict, lead_days: int, days_window: int) -> dict`.
"""

import numpy as np

def process_location_data(location_features_dict: dict, labels: dict, lead_days: int, days_window: int) -> dict:
    processed_data = {}

    # Sort common locations for clarity
    common_locations = sorted(list(location_features_dict.keys()))

    for common_location in common_locations:
        # Get data and labels
        X, y = location_features_dict[common_location], labels[common_location]
        X, y = np.array(X), np.array(y)

        # Eliminate last days to match labels.shape
        X = X[:-(lead_days + days_window)]

        processed_data[common_location] = (X, y)

    return processed_data