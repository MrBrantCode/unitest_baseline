"""
QUESTION:
Calculate the ratio of the total time required for executing a compilation on a diskless workstation against a workstation with a local disk. The compilation requires 30 seconds of active computation and 200 file page accesses. The average access time for each page over the network is 0.1 second, and via local disk is 0.05 second. Computation and file access activities are not overlapped.
"""

def calculate_execution_time_ratio(avg_network_time, avg_local_disk_time, compilation_time, file_page_accesses):
    """
    Calculate the ratio of the total time required for executing a compilation 
    on a diskless workstation against a workstation with a local disk.

    Args:
    - avg_network_time (float): Average access time over network in seconds
    - avg_local_disk_time (float): Average access time via local disk in seconds
    - compilation_time (float): Compilation activity computation time in seconds
    - file_page_accesses (int): Number of file page accesses

    Returns:
    - ratio (float): Ratio of total execution times
    """
    total_network_time = compilation_time + (avg_network_time * file_page_accesses)
    total_local_disk_time = compilation_time + (avg_local_disk_time * file_page_accesses)
    ratio = total_network_time / total_local_disk_time
    return ratio