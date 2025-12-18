"""
QUESTION:
Implement a `HashMap` class with a fixed size that uses separate chaining for collision resolution. The class should have the following methods: `__init__(size)`, `put(key, value)`, `get(key)`, and `remove(key)`. The `put(key, value)` method inserts or updates a key-value pair, the `get(key)` method returns the value associated with the given key (or -1 if the key does not exist), and the `remove(key)` method removes the key and its associated value. The hash function is based on the modulo of the key's hash code with the size of the hash map.
"""

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def entance(size):
    class HashMap:
        def __init__(self, size):
            self.size = size
            self.map = [None] * size

        def put(self, key, value):
            index = hash(key) % self.size
            if self.map[index] is None:
                self.map[index] = ListNode(key, value)
            else:
                current = self.map[index]
                while current:
                    if current.key == key:
                        current.value = value
                        return
                    if current.next is None:
                        break
                    current = current.next
                current.next = ListNode(key, value)

        def get(self, key):
            index = hash(key) % self.size
            current = self.map[index]
            while current:
                if current.key == key:
                    return current.value
                current = current.next
            return -1

        def remove(self, key):
            index = hash(key) % self.size
            current = self.map[index]
            prev = None
            while current:
                if current.key == key:
                    if prev:
                        prev.next = current.next
                    else:
                        self.map[index] = current.next
                    return
                prev = current
                current = current.next
    return HashMap(size)