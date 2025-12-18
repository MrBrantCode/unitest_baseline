"""
QUESTION:
Write a function called `calculate_compression_efficiency` that calculates the efficiency of a given compression technique in terms of storage, network, and cost. The function should take in the original file size, the compressed file size, and the network transfer speed as parameters. The function should return a dictionary containing the storage efficiency, network efficiency, and cost efficiency of the compression technique.
"""

def calculate_compression_efficiency(original_size, compressed_size, network_speed):
    """
    Calculate the efficiency of a compression technique in terms of storage, network, and cost.

    Args:
        original_size (float): The original size of the file in bytes.
        compressed_size (float): The compressed size of the file in bytes.
        network_speed (float): The network transfer speed in bytes per second.

    Returns:
        dict: A dictionary containing the storage efficiency, network efficiency, and cost efficiency.
    """

    # Calculate storage efficiency as a percentage
    storage_efficiency = (1 - (compressed_size / original_size)) * 100

    # Calculate network efficiency in terms of transfer time
    original_transfer_time = original_size / network_speed
    compressed_transfer_time = compressed_size / network_speed
    network_efficiency = (1 - (compressed_transfer_time / original_transfer_time)) * 100

    # Calculate cost efficiency, assuming cost is directly proportional to storage and network usage
    cost_efficiency = (storage_efficiency + network_efficiency) / 2

    return {
        "storage_efficiency": storage_efficiency,
        "network_efficiency": network_efficiency,
        "cost_efficiency": cost_efficiency
    }