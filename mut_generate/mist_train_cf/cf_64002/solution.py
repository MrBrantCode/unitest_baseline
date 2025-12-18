"""
QUESTION:
Implement a function `access_block(block)` that simulates direct mapping of a cache and returns a boolean indicating whether the block is a cache hit. Assume a cache of size 5 lines, initially empty, and blocks are mapped to cache lines using the modulo operator.
"""

def access_block(block, cache):
    """
    Simulates direct mapping of a cache and returns a boolean indicating whether the block is a cache hit.

    Args:
    block (int): The block to be accessed.
    cache (list): The cache with 5 lines, initially empty.

    Returns:
    bool: True if the block is a cache hit, False otherwise.
    """
    index = block % len(cache)
    if cache[index] == block: # Cache hit
        return True
    else: # Cache miss
        cache[index] = block
        return False