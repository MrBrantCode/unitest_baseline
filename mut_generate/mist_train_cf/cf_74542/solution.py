"""
QUESTION:
Implement a function called `distributed_merge_sort` that takes a list of integers as input, representing a massive dataset to be sorted in a distributed system. The function should divide the dataset into smaller partitions, sort each partition using a local sorting algorithm, and then merge the sorted partitions into a single sorted list. The function should achieve a time complexity of O(n log n) and minimize data movement between nodes. Assume that each node in the distributed system can fit its partition of the data in its local memory.
"""

def distributed_merge_sort(data, num_partitions):
    """
    Sorts a massive dataset in a distributed system by dividing it into smaller partitions, 
    sorting each partition using local sorting algorithm, and then merging the sorted partitions.

    Args:
        data (list): The list of integers to be sorted.
        num_partitions (int): The number of partitions to divide the data into.

    Returns:
        list: A single sorted list of integers.
    """

    # Divide the data into smaller partitions
    partition_size = len(data) // num_partitions
    partitions = [data[i * partition_size:(i + 1) * partition_size] for i in range(num_partitions - 1)]
    partitions.append(data[(num_partitions - 1) * partition_size:])

    # Sort each partition using local sorting algorithm
    sorted_partitions = [sorted(partition) for partition in partitions]

    # Merge the sorted partitions
    return merge_partitions(sorted_partitions)


def merge_partitions(partitions):
    """
    Merges multiple sorted partitions into a single sorted list.

    Args:
        partitions (list): A list of sorted lists to be merged.

    Returns:
        list: A single sorted list.
    """
    result = []
    while any(partition for partition in partitions):
        min_val = float('inf')
        min_partition_index = -1
        for i, partition in enumerate(partitions):
            if partition and partition[0] < min_val:
                min_val = partition[0]
                min_partition_index = i
        result.append(min_val)
        partitions[min_partition_index] = partitions[min_partition_index][1:]
    return result