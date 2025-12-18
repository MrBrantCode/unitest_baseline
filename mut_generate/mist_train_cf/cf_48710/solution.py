"""
QUESTION:
Write a function called `manage_data_skew` that optimizes data partitioning to handle data skew in Hadoop operations. Ensure the function balances the workload distribution across different reducers.
"""

def manage_data_skew(data, partition_strategy='round-robin'):
    """
    Optimizes data partitioning to handle data skew in Hadoop operations.

    Args:
        data (list): The data to be partitioned.
        partition_strategy (str): The partitioning strategy to use. Defaults to 'round-robin'.

    Returns:
        dict: A dictionary with the partitioned data.
    """

    # Check if the data is empty
    if not data:
        return {}

    # Initialize the partitions dictionary
    partitions = {}

    # Apply the round-robin partitioning strategy
    if partition_strategy == 'round-robin':
        # Calculate the number of reducers
        num_reducers = 4  # Assuming 4 reducers for simplicity

        # Partition the data across the reducers
        for i, item in enumerate(data):
            reducer_id = i % num_reducers
            if reducer_id not in partitions:
                partitions[reducer_id] = []
            partitions[reducer_id].append(item)

    # Apply the hash partitioning strategy
    elif partition_strategy == 'hash':
        # Import the hashlib library for hash calculation
        import hashlib

        # Partition the data based on the hash value of each item
        for item in data:
            hash_value = int(hashlib.md5(str(item).encode()).hexdigest(), 16)
            reducer_id = hash_value % 4  # Assuming 4 reducers for simplicity
            if reducer_id not in partitions:
                partitions[reducer_id] = []
            partitions[reducer_id].append(item)

    # Apply the range partitioning strategy
    elif partition_strategy == 'range':
        # Calculate the range for each reducer
        range_size = len(data) // 4  # Assuming 4 reducers for simplicity

        # Partition the data based on the range
        for i, item in enumerate(data):
            reducer_id = i // range_size
            if reducer_id not in partitions:
                partitions[reducer_id] = []
            partitions[reducer_id].append(item)

    return partitions