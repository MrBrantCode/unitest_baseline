"""
QUESTION:
Write a function `manage_data_skew` to optimize data distribution among Hadoop clusters and prevent data skew. The function should take in a list of task sizes and return a dictionary with optimized task distribution among clusters. The function should also handle cases where the number of reducers is fixed and the task sizes vary greatly. 

The function should minimize the difference in total task size among clusters. The number of reducers is not fixed and can be adjusted to achieve optimal task distribution. The function should not use any external libraries. 

The function should return a dictionary where the keys are the cluster IDs and the values are lists of task sizes assigned to each cluster.
"""

def manage_data_skew(task_sizes):
    """
    This function optimizes data distribution among Hadoop clusters and prevents data skew.
    
    Parameters:
    task_sizes (list): A list of task sizes.
    
    Returns:
    dict: A dictionary where the keys are the cluster IDs and the values are lists of task sizes assigned to each cluster.
    """
    
    # Sort the task sizes in descending order
    task_sizes.sort(reverse=True)
    
    # Initialize a dictionary to store the task distribution
    task_distribution = {}
    
    # Initialize the cluster ID
    cluster_id = 0
    
    # Initialize the total task size for the current cluster
    total_task_size = 0
    
    # Iterate over the task sizes
    for task_size in task_sizes:
        # If the task size is greater than the total task size of the current cluster, 
        # assign the task to a new cluster
        if task_size > total_task_size:
            cluster_id += 1
            total_task_size = 0
            task_distribution[cluster_id] = [task_size]
        # Otherwise, assign the task to the current cluster
        else:
            task_distribution.setdefault(cluster_id, []).append(task_size)
            total_task_size += task_size
    
    return task_distribution