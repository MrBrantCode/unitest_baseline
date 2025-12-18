"""
QUESTION:
Design a function called `get_migration_threshold` that determines the migration threshold value in a MongoDB sharded cluster, considering the actual data size rather than the number of chunks, for MongoDB versions 6.0 and later. 

The function should take the chunk size in MB and the number of chunks as input and return the corresponding migration threshold value based on the new dynamic decision-making criteria involving data size and distribution.
"""

def get_migration_threshold(chunk_size_mb, num_chunks):
    """
    Calculate the migration threshold value for a MongoDB sharded cluster.
    
    Parameters:
    chunk_size_mb (int): The chunk size in megabytes.
    num_chunks (int): The number of chunks.
    
    Returns:
    int: The migration threshold value.
    """
    
    # Define a threshold for the minimum number of chunks
    min_chunks_threshold = 2
    
    # Define a threshold for the maximum chunk size
    max_chunk_size_threshold_mb = 128
    
    # Check if the number of chunks is below the minimum threshold
    if num_chunks < min_chunks_threshold:
        # Return a migration threshold value of 0
        return 0
    
    # Calculate the total data size
    total_data_size_mb = chunk_size_mb * num_chunks
    
    # Define a threshold for the total data size
    total_data_size_threshold_mb = 1024
    
    # Check if the total data size is above the threshold
    if total_data_size_mb > total_data_size_threshold_mb:
        # Return a migration threshold value of 0.5 (50%)
        return 0.5
    
    # If none of the above conditions are met, return a migration threshold value of 0.2 (20%)
    return 0.2