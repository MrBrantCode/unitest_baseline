"""
QUESTION:
Implement a function `fast_search` that can efficiently search through approximately 10^9 elements, achieving a search time of less than 1 millisecond while minimizing memory usage.
"""

def fast_search(elements, target):
    # Create a hash table (dictionary in Python) to store the elements for fast lookup
    hash_table = {element: True for element in elements}
    
    # Use the hash table to search for the target element
    return target in hash_table