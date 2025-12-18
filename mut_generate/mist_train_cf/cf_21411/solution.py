"""
QUESTION:
Implement a data structure with the following methods: `insert(key, value)`, `get(key)`, `delete(key)`, `exists(key)`, `get_sorted_keys()`, and `get_num_elements()`. 

The `insert(key, value)` method should add a key-value pair to the data structure and return a success message if the key does not already exist. The `get(key)` method should return the value associated with the given key. The `delete(key)` method should remove the key-value pair and return the deleted value. The `exists(key)` method should return a boolean indicating whether the key exists in the data structure. The `get_sorted_keys()` method should return all keys in sorted order. The `get_num_elements()` method should return the number of elements in the data structure.

The time complexities for these methods are as follows: `insert(key, value)` - O(1), `get(key)` - O(1), `delete(key)` - O(1), `exists(key)` - O(1), `get_sorted_keys()` - O(n log n), and `get_num_elements()` - O(1). The space complexities are as follows: `insert(key, value)` - O(n), `get(key)` - O(1), `delete(key)` - O(1), `exists(key)` - O(1), `get_sorted_keys()` - O(n), and `get_num_elements()` - O(1).
"""

def entance(key, value):
    data = {}
    keys = []

    def insert(key, value):
        if key in data:
            return "Key already exists"
        data[key] = value
        keys.append(key)
        return "Insertion successful"

    def get(key):
        if key not in data:
            return "Key does not exist"
        return data[key]

    def delete(key):
        if key not in data:
            return "Key does not exist"
        value = data[key]
        del data[key]
        keys.remove(key)
        return value

    def exists(key):
        return key in data

    def get_sorted_keys():
        return sorted(keys)

    def get_num_elements():
        return len(data)

    # return the functions
    return locals()