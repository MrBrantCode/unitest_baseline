"""
QUESTION:
Implement a function `process_columns` that takes a `dataset` and a `ColumnMapping` object as input. The function should return a `Columns` object containing `utility_columns` and a sorted list of `num_feature_names`. Ensure the returned `num_feature_names` are in ascending order.
"""

class Columns:
    def __init__(self, utility_columns, num_feature_names):
        self.utility_columns = utility_columns
        self.num_feature_names = sorted(num_feature_names)


def process_columns(dataset, column_mapping):
    # Process the dataset and column_mapping to extract utility columns and numerical feature names
    # Ensure that the numerical feature names are sorted before returning

    # Example implementation:
    num_feature_names = ['feature2', 'feature1']  # Placeholder for extracting numerical feature names
    utility_columns = None  # Placeholder for extracting utility columns
    return Columns(utility_columns, num_feature_names)