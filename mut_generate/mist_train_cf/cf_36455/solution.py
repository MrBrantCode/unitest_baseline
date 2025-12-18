"""
QUESTION:
Implement a hash table using separate chaining with the following methods: 

* `insert(key, value)`: Insert a key-value pair into the hash table.
* `get(key)`: Retrieve the value associated with a given key.
* `delete(key)`: Remove the key-value pair associated with the given key.

The hash table should be initialized with a given size. The `insert`, `get`, and `delete` methods should handle collisions using separate chaining, where each bucket in the hash table is a linked list of key-value pairs.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def entrance(size):
    class HashTable:
        def __init__(self):
            self.size = size
            self.seghash = {}

        def insert(self, key, value):
            hash_code = hash(key) % self.size
            if hash_code not in self.seghash:
                self.seghash[hash_code] = Node(key, value)
            else:
                current = self.seghash[hash_code]
                while current.next:
                    if current.key == key:
                        current.value = value
                        return
                    current = current.next
                current.next = Node(key, value)

        def get(self, key):
            hash_code = hash(key) % self.size
            if hash_code in self.seghash:
                current = self.seghash[hash_code]
                while current:
                    if current.key == key:
                        return current.value
                    current = current.next
            return None

        def delete(self, key):
            hash_code = hash(key) % self.size
            if hash_code in self.seghash:
                prev = None
                current = self.seghash[hash_code]
                while current:
                    if current.key == key:
                        if prev:
                            prev.next = current.next
                        else:
                            self.seghash[hash_code] = current.next
                        return
                    prev = current
                    current = current.next
    return HashTable()