"""
QUESTION:
Create a function called `convert_to_hex_doubly_linked_list` that takes a string as input, converts each character to its corresponding hexadecimal byte representation, and stores these hexadecimal bytes in a doubly-linked list. The function should return the doubly-linked list. The input string will only contain ASCII characters.
"""

import array

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

def convert_to_hex_doubly_linked_list(input_string):
    """
    This function takes a string as input, converts each character to its corresponding hexadecimal byte representation, 
    and stores these hexadecimal bytes in a doubly-linked list.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        DoublyLinkedList: A doubly-linked list containing the hexadecimal byte representations of the input string.
    """

    # Convert string to hexadecimal values, store them as an array.
    hex_array = array.array('B', input_string.encode())
    hex_values = [hex(i) for i in hex_array.tolist()]

    # Create a doubly linked list and append the hex values.
    dll = DoublyLinkedList()
    for value in hex_values:
        dll.append(value)

    return dll