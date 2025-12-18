"""
QUESTION:
Implement a Python function named `hadoop_data_replication` that takes a Hadoop cluster's replication factor and a list of DataNodes as input, and returns a dictionary with the following keys: 'replication_factor', 'nodes_with_replicated_data', 'nodes_with_under_replicated_data', and 'nodes_with_over_replicated_data'. The function should also consider the impact on system performance and data integrity.
"""

def hadoop_data_replication(replication_factor, data_nodes):
    """
    This function takes a Hadoop cluster's replication factor and a list of DataNodes as input, 
    and returns a dictionary with the following keys: 'replication_factor', 'nodes_with_replicated_data', 
    'nodes_with_under_replicated_data', and 'nodes_with_over_replicated_data'.

    Args:
        replication_factor (int): The replication factor of the Hadoop cluster.
        data_nodes (list): A list of DataNodes in the Hadoop cluster.

    Returns:
        dict: A dictionary containing the replication factor, nodes with replicated data, 
              nodes with under-replicated data, and nodes with over-replicated data.
    """

    # Initialize an empty dictionary to store the results
    result = {
        'replication_factor': replication_factor,
        'nodes_with_replicated_data': [],
        'nodes_with_under_replicated_data': [],
        'nodes_with_over_replicated_data': []
    }

    # Iterate over each DataNode
    for node in data_nodes:
        # Assuming each DataNode is a dictionary with a 'name' key and a 'replication' key
        if node['replication'] == replication_factor:
            # If the node's replication matches the replication factor, add it to the list of nodes with replicated data
            result['nodes_with_replicated_data'].append(node['name'])
        elif node['replication'] < replication_factor:
            # If the node's replication is less than the replication factor, add it to the list of nodes with under-replicated data
            result['nodes_with_under_replicated_data'].append(node['name'])
        else:
            # If the node's replication is greater than the replication factor, add it to the list of nodes with over-replicated data
            result['nodes_with_over_replicated_data'].append(node['name'])

    return result