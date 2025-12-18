"""
QUESTION:
Design a function `prevent_data_skew` to prevent data skew in Hadoop by ensuring even distribution of data across nodes in a Hadoop cluster. The function should accept a list of file sizes as input and return a partitioning plan that minimizes data skew.
"""

def prevent_data_skew(file_sizes):
    """
    This function prevents data skew in Hadoop by ensuring even distribution of data across nodes in a Hadoop cluster.

    Args:
        file_sizes (list): A list of file sizes.

    Returns:
        list: A partitioning plan that minimizes data skew.
    """

    # Sort the file sizes in descending order to prioritize larger files
    file_sizes.sort(reverse=True)
    
    # Initialize the partitioning plan with empty lists for each node
    num_nodes = len(file_sizes)
    partitioning_plan = [[] for _ in range(num_nodes)]
    
    # Distribute the files across nodes in a round-robin manner
    for i, file_size in enumerate(file_sizes):
        partitioning_plan[i % num_nodes].append(file_size)
    
    return partitioning_plan