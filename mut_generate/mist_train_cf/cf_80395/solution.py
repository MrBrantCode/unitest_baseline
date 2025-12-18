"""
QUESTION:
Implement a function `reduce_false_positives` to effectively reduce the false positive rate of a Bloom filter without generating any false negatives. The function should take as input the size of the Bloom filter (number of bits), the number of hash functions used, and the number of elements inserted into the filter. The function should use one or more of the following methods: increasing the size of the Bloom filter, choosing the optimal number of hash functions, using a counting Bloom filter, layered Bloom filters or Bloom filter hierarchies, or partitioned Bloom filters.
"""

import math

def reduce_false_positives(size, num_hash_functions, num_elements):
    """
    Reduce the false positive rate of a Bloom filter without generating any false negatives.
    
    Parameters:
    size (int): The size of the Bloom filter (number of bits).
    num_hash_functions (int): The number of hash functions used.
    num_elements (int): The number of elements inserted into the filter.
    
    Returns:
    int: The optimal number of hash functions.
    """
    
    # Calculate the optimal number of hash functions
    optimal_hash_functions = (size / num_elements) * math.log(2)
    
    # Round up to the nearest integer, since we can't have a fraction of a hash function
    optimal_hash_functions = math.ceil(optimal_hash_functions)
    
    return optimal_hash_functions