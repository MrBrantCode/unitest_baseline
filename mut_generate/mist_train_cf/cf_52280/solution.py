"""
QUESTION:
The function `custom_partitioner` should take a list of items and the number of partitions as input and return a dictionary where the keys are the partition numbers and the values are the lists of items assigned to each partition. The function should aim to distribute the items as evenly as possible among the partitions.
"""

def custom_partitioner(items, partitions):
    # Calculate the size of each partition
    partition_size = len(items) // partitions
    remainder = len(items) % partitions

    # Initialize the dictionary to store the partitions
    partitions_dict = {}

    # Initialize the start index
    start = 0

    # Loop over the partitions
    for i in range(partitions):
        # Calculate the end index
        end = start + partition_size + (1 if i < remainder else 0)

        # Assign the items to the current partition
        partitions_dict[i] = items[start:end]

        # Update the start index
        start = end

    return partitions_dict