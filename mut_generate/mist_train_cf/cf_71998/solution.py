"""
QUESTION:
Write a function named `optimize_data_locality` that optimizes data locality in a Spark operation to prevent bottlenecks and improve efficiency. The function should take into account the levels of data locality (PROCESS_LOCAL, NODE_LOCAL, NO_PREF, RACK_LOCAL, or ANY) and the factors that contribute to data locality bottlenecks, such as insufficient cores, inefficient data partitioning, and scheduling delays. The function should return the optimized data locality configuration.
"""

def optimize_data_locality(data_partitions, available_cores, locality_preference):
    """
    Optimizes data locality by adjusting data partitions and cores based on the given locality preference.

    Args:
        data_partitions (int): The number of data partitions.
        available_cores (int): The number of available cores.
        locality_preference (str): The preferred level of data locality (PROCESS_LOCAL, NODE_LOCAL, NO_PREF, RACK_LOCAL, or ANY).

    Returns:
        dict: A dictionary containing the optimized data locality configuration.
    """
    # Calculate the ideal number of cores per partition
    ideal_cores_per_partition = available_cores // data_partitions
    
    # Adjust data partitions based on the preferred locality level
    if locality_preference == "PROCESS_LOCAL":
        # For PROCESS_LOCAL, try to allocate at least one core per partition
        adjusted_partitions = min(data_partitions, available_cores)
    elif locality_preference == "NODE_LOCAL":
        # For NODE_LOCAL, try to allocate cores in batches of 2-4 per partition
        adjusted_partitions = max(1, data_partitions // 2)
    else:
        # For other locality levels, use the original number of partitions
        adjusted_partitions = data_partitions
    
    # Calculate the optimized data locality configuration
    optimized_config = {
        "data_partitions": adjusted_partitions,
        "cores_per_partition": ideal_cores_per_partition,
        "locality_level": locality_preference
    }
    
    return optimized_config