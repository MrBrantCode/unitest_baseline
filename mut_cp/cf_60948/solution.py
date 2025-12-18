"""
ORIGINAL QUESTION:
Increase the capacity of an Amazon Redshift cluster and optimize its performance to handle massive data volumes when encountering a DiskFullError.

Create a function `optimize_redshift_performance` that implements the following strategies: 
- Upsize the cluster by adding more nodes to increase storage and improve performance
- Implement columnar compression to save storage space
- Archive historical data to offload less frequently accessed data to cheaper storage solutions

Note that the function should not be implemented, only a description of what it should do.
"""

def optimize_redshift_performance(cluster):
    """
    Optimizes the performance of an Amazon Redshift cluster by upscaling the cluster,
    implementing columnar compression, and archiving historical data.

    Args:
        cluster (dict): A dictionary containing information about the Redshift cluster.

    Returns:
        dict: A dictionary containing information about the optimized Redshift cluster.
    """

    # Upsize the cluster by adding more nodes to increase storage and improve performance
    # Add more nodes to the cluster
    cluster['nodes'] += 1  # Assuming nodes is a key in the cluster dictionary

    # Implement columnar compression to save storage space
    # Apply compression to all columns in the cluster
    cluster['compression'] = 'columnar'

    # Archive historical data to offload less frequently accessed data to cheaper storage solutions
    # Move historical data to a cheaper storage solution like S3 or Glacier
    cluster['archive'] = 'historical_data'

    return cluster