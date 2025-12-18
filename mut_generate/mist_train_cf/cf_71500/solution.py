"""
QUESTION:
Create a function named `concatenate_strings` that takes two string parameters, `str1` and `str2`, and returns their concatenated string by utilizing the logic of singly linked lists. Each node in the linked list should store a single character of the input strings. Define the necessary data structures and functions to create nodes, insert new nodes, and print the concatenated string from the linked list. The function should not use built-in string concatenation operators.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end='')
            curr_node = curr_node.next
        print()

def concatenate_strings(str1, str2):
    linked_list = LinkedList()

    for char in str1:
        node = Node(char)
        linked_list.insert(node)
    
    for char in str2:
        node = Node(char)
        linked_list.insert(node)

    result = ''
    curr_node = linked_list.head
    while curr_node:
        result += curr_node.data
        curr_node = curr_node.next
    return result