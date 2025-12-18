"""
QUESTION:
Implement a function `create_linked_list_from_text` that takes a string as input, removes punctuation, splits it into individual words, and stores these words in a linked list. The function should return the linked list. The linked list should be implemented with a `Node` class for individual nodes and a `LinkedList` class for the full list. The `LinkedList` class should have an `append` method to add words to the list and a `display` method to print the list.
"""

import string

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def display(self):
        elems = []
        curr_node = self.head
        while curr_node:
            elems.append(curr_node.data)
            curr_node = curr_node.next
        print(elems)

def create_linked_list_from_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    linked_list = LinkedList()
    for word in text.split():
        linked_list.append(word)
    return linked_list