"""
QUESTION:
Write a function called `hashTableLookup(hashTable, key)` that takes a hash table and a key as input and returns the associated value if the key exists in the hash table. The function should handle collisions using chaining. Assume the hash table is implemented as an array where each index can store either a key-value pair or a list of key-value pairs in case of a collision. The function should return "Key Not Found" if the key does not exist in the hash table.
"""

def hashTableLookup(hashTable, key):
    """
    This function performs a lookup operation on a given hash table to find the value associated with a specific key.

    Args:
        hashTable (list): The hash table to search in.
        key: The key to search for in the hash table.

    Returns:
        The value associated with the key if found; otherwise, "Key Not Found".
    """

    # Assuming the hash function is a simple modulo operation
    index = hash(key) % len(hashTable)

    # Check if the key exists at this index in hash table
    if isinstance(hashTable[index], list):
        # If hashTable[index] is a list, iterate through the list to find the matching key
        for pair in hashTable[index]:
            if pair[0] == key:
                return pair[1]
        # If not found in the list, return “Key Not Found”
        return "Key Not Found"
    else:
        # If the hashTable[index] is not a list, simply compare the key at hashTable[index] with the given key
        if hashTable[index] is not None and hashTable[index][0] == key:
            return hashTable[index][1]
        # If not found, return “Key Not Found”
        return "Key Not Found"