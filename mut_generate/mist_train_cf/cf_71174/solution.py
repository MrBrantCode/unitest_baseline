"""
QUESTION:
Implement a hash table with the following functions: `insert(key, value)`, `search(key)`, and `delete(key)`. The hash table should be able to store key-value pairs, retrieve the value associated with a given key, and delete a key-value pair. The functions should handle cases where the key does not exist in the hash table without raising an error.
"""

def entrance(key, value=None, delete=False):
    hash_table = entrance.hash_table
    if delete:
        if key in hash_table:
            del hash_table[key]
    elif value is not None:
        hash_table[key] = value
    else:
        return hash_table.get(key)

entrance.hash_table = {}