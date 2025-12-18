"""
QUESTION:
Implement the function `reduce_data_skew` to mitigate data skew in Hadoop clusters. This function should take in two parameters: `data` (a dictionary where keys are node IDs and values are lists of data) and `partition_keys` (a list of new partition keys). It should return a new dictionary where data is redistributed across the cluster using the provided partition keys. 

The function should be able to handle cases where certain keys are more prevalent than others, and it should aim to achieve an even distribution of data across the cluster. You can use partitioning techniques such as range partitioning, consistent hashing, or round-robin distribution to achieve this.
"""

def reduce_data_skew(data, partition_keys):
    """
    Redistribute data across the cluster using the provided partition keys to mitigate data skew.

    Args:
        data (dict): A dictionary where keys are node IDs and values are lists of data.
        partition_keys (list): A list of new partition keys.

    Returns:
        dict: A new dictionary where data is redistributed across the cluster.
    """
    
    # Initialize an empty dictionary to store the redistributed data
    redistributed_data = {key: [] for key in partition_keys}
    
    # Iterate over each node in the data
    for node_id, values in data.items():
        # Iterate over each value in the node
        for value in values:
            # Calculate the partition key for the value using round-robin distribution
            partition_key_index = hash(value) % len(partition_keys)
            partition_key = partition_keys[partition_key_index]
            
            # Add the value to the corresponding partition key in the redistributed data
            redistributed_data[partition_key].append(value)
    
    return redistributed_data