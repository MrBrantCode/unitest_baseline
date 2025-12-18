"""
QUESTION:
Calculate the estimated ratio of time needed to read a significant file when the block retrieval size increases from 1,000 bytes/block to 4,000 bytes/block. The function should be named `estimated_time_ratio`. 

Assume a single file-read operation is divided into four segments: disk seek time, disk latency time, disk transfer time, and operating system overhead. Note that the exact time each segment requires and the total reading a "significant file" constitutes are unknown, so provide a general solution based on the improvement in block size.
"""

def estimated_time_ratio(original_block_size, new_block_size):
    """
    Calculate the estimated ratio of time needed to read a significant file 
    when the block retrieval size increases.

    Args:
    original_block_size (int): The original block size in bytes.
    new_block_size (int): The new block size in bytes.

    Returns:
    float: The estimated time ratio.
    """
    return original_block_size / new_block_size

# Usage:
# estimated_ratio = estimated_time_ratio(1000, 4000)
# print(estimated_ratio)