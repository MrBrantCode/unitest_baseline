"""
QUESTION:
### Optimize Data Locality in Apache Spark

Write a function called `optimize_data_locality` to determine the optimal data locality level in Apache Spark for a given set of parameters. The function should consider the trade-offs between PROCESS_LOCAL, NODE_LOCAL, NO_PREF, RACK_LOCAL, and ANY data locality levels and recommend the most suitable level based on the input parameters. 

The function should take as input the size of the data, the number of partitions, and the cluster configuration (number of nodes and cores per node). The function should return the recommended data locality level.
"""

def optimize_data_locality(data_size, num_partitions, num_nodes, cores_per_node):
    """
    Determine the optimal data locality level in Apache Spark for a given set of parameters.

    Parameters:
    data_size (int): Size of the data
    num_partitions (int): Number of partitions
    num_nodes (int): Number of nodes in the cluster
    cores_per_node (int): Number of cores per node

    Returns:
    str: Recommended data locality level (PROCESS_LOCAL, NODE_LOCAL, NO_PREF, RACK_LOCAL, ANY)
    """
    
    # Calculate the data size per partition
    data_size_per_partition = data_size / num_partitions
    
    # If data size per partition is small, PROCESS_LOCAL is optimal
    if data_size_per_partition < 100 * 1024 * 1024:  # 100 MB
        return "PROCESS_LOCAL"
    
    # If data size per partition is medium, NODE_LOCAL is optimal
    elif data_size_per_partition < 1 * 1024 * 1024 * 1024:  # 1 GB
        return "NODE_LOCAL"
    
    # If data size per partition is large, NO_PREF is optimal
    elif data_size_per_partition < 10 * 1024 * 1024 * 1024:  # 10 GB
        return "NO_PREF"
    
    # If number of nodes is large, RACK_LOCAL is optimal
    elif num_nodes > 100:
        return "RACK_LOCAL"
    
    # If none of the above conditions are met, ANY is optimal
    else:
        return "ANY"