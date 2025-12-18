"""
QUESTION:
Implement a function named `hash_table` that stores data items in an associative array where the key is used to quickly search for the data item.
"""

def hash_table(size):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    table = [None] * size

    def put(key, value):
        index = hash(key) % size
        if table[index] is None:
            table[index] = Node(key, value)
        else:
            node = table[index]
            while node.next:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = Node(key, value)

    def get(key):
        index = hash(key) % size
        node = table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    return put, get