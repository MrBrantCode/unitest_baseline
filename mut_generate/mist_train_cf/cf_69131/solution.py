"""
QUESTION:
Create a function called `linked_list_to_hash_table` that takes a linked list as input. The function should return a hash table where each node's data serves as the key and its occurrence as the value. The input linked list is a singly linked list with nodes containing integer data. The hash table should be implemented as a dictionary.
"""

def linked_list_to_hash_table(linked_list):
    hash_table = {}
    node = linked_list.head
    while node is not None:
        if node.data in hash_table:
            hash_table[node.data] += 1
        else:
            hash_table[node.data] = 1
        node = node.next
    return hash_table