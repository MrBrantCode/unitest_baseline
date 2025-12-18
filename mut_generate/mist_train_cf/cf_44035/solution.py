"""
QUESTION:
Write a function called `distribute_data` to manage data skew in a Hadoop operation. The function should take a list of data as input and return a dictionary where the keys are the node IDs and the values are the data distributed across these nodes. The goal is to distribute the data as evenly as possible to prevent data skew.
"""

def distribute_data(data, num_nodes):
    """
    Distributes data across nodes to prevent data skew.

    Args:
        data (list): The list of data to be distributed.
        num_nodes (int): The number of nodes to distribute the data across.

    Returns:
        dict: A dictionary where the keys are the node IDs and the values are the data distributed across these nodes.
    """
    # Calculate the size of each chunk
    chunk_size = len(data) // num_nodes
    
    # Distribute the data across the nodes
    distributed_data = {}
    for i in range(num_nodes):
        start = i * chunk_size
        end = start + chunk_size
        if i == num_nodes - 1:
            end = len(data)
        distributed_data[f'Node {i+1}'] = data[start:end]
    
    return distributed_data