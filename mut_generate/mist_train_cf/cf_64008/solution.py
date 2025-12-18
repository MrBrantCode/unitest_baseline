"""
QUESTION:
Implement a `manage_data_skew` function to mitigate data skew in a Hadoop ecosystem. The function should accept a list of data chunks and the number of nodes in the cluster as input. It should return a dictionary where the keys are the node IDs and the values are lists of data chunks assigned to each node. The goal is to distribute the data chunks as evenly as possible across the nodes to prevent data skew. The function should be able to handle different Hadoop versions and supplementary libraries, and ensure data consistency and truthfulness.
"""

def manage_data_skew(data_chunks, num_nodes):
    """
    Mitigate data skew in a Hadoop ecosystem by distributing data chunks evenly across nodes.

    Args:
        data_chunks (list): List of data chunks to be distributed.
        num_nodes (int): Number of nodes in the cluster.

    Returns:
        dict: Dictionary where keys are node IDs and values are lists of data chunks assigned to each node.
    """
    # Calculate the ideal number of chunks per node
    chunks_per_node = len(data_chunks) // num_nodes
    
    # Initialize a dictionary to store the assigned chunks for each node
    assigned_chunks = {node_id: [] for node_id in range(num_nodes)}
    
    # Distribute the data chunks across the nodes
    for i, chunk in enumerate(data_chunks):
        node_id = i % num_nodes
        assigned_chunks[node_id].append(chunk)
    
    return assigned_chunks