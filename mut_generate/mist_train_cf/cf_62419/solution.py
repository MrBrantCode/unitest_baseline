"""
QUESTION:
Create a function `calculate_data_skew` that determines the degree of data skew in a Hadoop environment given a list of node capacities and a list of task sizes. The function should return a float value representing the skew factor, which is calculated as the ratio of the maximum task size to the average node capacity.
"""

def calculate_data_skew(node_capacities, task_sizes):
    """
    Calculate the data skew factor in a Hadoop environment.

    Args:
    node_capacities (list): A list of node capacities.
    task_sizes (list): A list of task sizes.

    Returns:
    float: The skew factor, calculated as the ratio of the maximum task size to the average node capacity.
    """
    if not node_capacities or not task_sizes:
        return 0.0
    
    avg_node_capacity = sum(node_capacities) / len(node_capacities)
    max_task_size = max(task_sizes)
    
    # Calculate the skew factor
    skew_factor = max_task_size / avg_node_capacity
    
    return skew_factor