"""
QUESTION:
Implement a function called `hash_table` that uses separate chaining to handle collisions between hash values. The function should take in a list of key-value pairs and return a hash table where each key-value pair is stored in a dictionary. If a collision occurs, append the new key-value pair to the existing list at the corresponding index. The hash function should use the modulo operator to map the keys to an index in the array. Assume the size of the hash table is 10.
"""

def hash_table(key_value_pairs):
    """
    Creates a hash table using separate chaining to handle collisions between hash values.

    Args:
        key_value_pairs (list): A list of key-value pairs to be stored in the hash table.

    Returns:
        list: A hash table where each key-value pair is stored in a dictionary.
    """
    hash_table = [[] for _ in range(10)]  # Initialize the hash table with 10 empty slots

    for key, value in key_value_pairs:
        index = hash(key) % 10  # Calculate the index using the modulo operator
        hash_table[index].append({key: value})  # Append the key-value pair to the corresponding slot

    return hash_table