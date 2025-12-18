"""
QUESTION:
Create a function `HashTable` that implements a hash table data structure in Python. The hash table should have methods `put(key, value)` and `get(key)` for storing and retrieving key-value pairs, respectively. The hash function should map keys to an index in an array using a sum of ASCII values modulo the size of the hash table. The implementation should handle collisions using separate chaining with buckets as lists. 

The hash table should have a fixed size, and the implementation should be able to handle cases where the key already exists in the bucket. The `get(key)` method should return `None` if the key is not found.
"""

def hash_table(size):
    table = [None] * size
    
    def _hash(key):
        return sum(ord(c) for c in key) % size
    
    def put(key, value):
        index = _hash(key)
        
        if table[index] is None:
            table[index] = []
        
        for i, (k, v) in enumerate(table[index]):
            if k == key:
                table[index][i] = (key, value)
                return
        
        table[index].append((key, value))
    
    def get(key):
        index = _hash(key)
        
        if table[index] is None:
            return None
        
        for k, v in table[index]:
            if k == key:
                return v
        
        return None
    
    return _hash, put, get