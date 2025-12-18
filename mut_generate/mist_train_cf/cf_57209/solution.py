"""
QUESTION:
Write a function `nodetool_status_latency` that calculates the total latency of the `nodetool status` command in a Cassandra cluster with remote JMX enabled. The function should take the number of nodes in the cluster, the average latency of a single network call, and a boolean indicating whether the command is run locally on a node or remotely as input. If the command is run remotely, the function should return the total latency, which is the average latency multiplied by the number of nodes. If the command is run locally, the function should return the average latency.
"""

def nodetool_status_latency(num_nodes, avg_latency, is_remote):
    """
    Calculates the total latency of the 'nodetool status' command in a Cassandra cluster.

    Args:
        num_nodes (int): The number of nodes in the cluster.
        avg_latency (float): The average latency of a single network call.
        is_remote (bool): A boolean indicating whether the command is run remotely or locally.

    Returns:
        float: The total latency of the command.
    """
    if is_remote:
        return num_nodes * avg_latency
    else:
        return avg_latency