"""
QUESTION:
Write a Python function named `determine_optimal_num_reducers` that takes two parameters: `dataset_size` and `available_resources`. The function should calculate and return the optimal number of reducers for a Hadoop job based on the provided dataset size and available resources, to mitigate data skew and ensure efficient batch processing. Assume the ideal reducer size is between 1GB and 5GB.
"""

def determine_optimal_num_reducers(dataset_size, available_resources):
    """
    Calculate the optimal number of reducers for a Hadoop job based on the provided dataset size and available resources.

    Args:
        dataset_size (float): The size of the dataset in GB.
        available_resources (float): The available resources in GB.

    Returns:
        int: The optimal number of reducers.
    """
    ideal_reducer_size = min(max(1, available_resources / 10), 5)  # ideal reducer size is between 1GB and 5GB
    optimal_num_reducers = int(dataset_size / ideal_reducer_size)
    return optimal_num_reducers