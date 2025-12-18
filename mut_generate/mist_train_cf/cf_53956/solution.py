"""
QUESTION:
Implement a function named 'detect_data_skew' to identify data skew in a Hadoop operation by checking if the data distribution is balanced across nodes. The function should take a list of node workloads as input and return 'True' if data skew is detected, 'False' otherwise. Assume that data skew exists if the maximum workload is more than twice the minimum workload.
"""

def detect_data_skew(node_workloads):
    """
    Identifies data skew in a Hadoop operation by checking if the data distribution is balanced across nodes.
    
    Args:
    node_workloads (list): A list of node workloads.
    
    Returns:
    bool: True if data skew is detected, False otherwise.
    """
    if not node_workloads:
        return False
    
    min_workload = min(node_workloads)
    max_workload = max(node_workloads)
    
    # Data skew exists if the maximum workload is more than twice the minimum workload
    return max_workload > 2 * min_workload