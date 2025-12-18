"""
QUESTION:
Implement a HashTable class with separate chaining collision resolution. The class should have the following methods:

- `__init__(self, size)`: Initializes the hash table with a specified size.
- `__hash(self, key)`: Computes the hash value for a given key.
- `insert(self, key, value)`: Inserts a key-value pair into the hash table.
- `retrieve(self, key)`: Retrieves the value associated with a given key.
- `delete(self, key)`: Deletes a key-value pair from the hash table.

Restrictions:
- The hash table should use separate chaining for collision resolution.
- The `retrieve` method should return `None` if the key is not found.
- The `delete` method should remove the key-value pair from the hash table if the key exists.
"""

def createHashTable(size):
    class HashTable:
        def __init__(self, size):
            self.size = size
            self.__buckets = [[] for _ in range(size)]

        def __hash(self, key):
            return hash(key) % self.size

        def insert(self, key, value):
            idx = self.__hash(key)
            self.__buckets[idx].append((key, value))

        def retrieve(self, key):
            idx = self.__hash(key)
            bucket = self.__buckets[idx]
            for k, v in bucket:
                if k == key:
                    return v
            return None  

        def delete(self, key):
            idx = self.__hash(key)
            bucket = self.__buckets[idx]
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    return

    return HashTable(size)