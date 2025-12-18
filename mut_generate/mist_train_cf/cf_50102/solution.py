"""
QUESTION:
Implement a function `address_data_skew` that takes a dictionary where the keys are node names and the values are lists of task sizes. The function should return a boolean indicating whether data skew exists (i.e., the maximum task size is more than twice the minimum task size) and a list of nodes with task sizes that are more than 1.5 times the average task size across all nodes.
"""

def address_data_skew(node_tasks):
    """
    This function checks for data skew in a dictionary of node tasks.

    Args:
    node_tasks (dict): A dictionary where keys are node names and values are lists of task sizes.

    Returns:
    tuple: A boolean indicating whether data skew exists and a list of nodes with task sizes more than 1.5 times the average task size.
    """

    # Combine all task sizes into a single list
    all_tasks = [task for tasks in node_tasks.values() for task in tasks]
    
    # Calculate the average task size
    avg_task_size = sum(all_tasks) / len(all_tasks)
    
    # Check if data skew exists (max task size > 2 * min task size)
    data_skew_exists = max(all_tasks) > 2 * min(all_tasks)
    
    # Identify nodes with task sizes more than 1.5 times the average task size
    skewed_nodes = [node for node, tasks in node_tasks.items() if any(task > 1.5 * avg_task_size for task in tasks)]
    
    return data_skew_exists, skewed_nodes