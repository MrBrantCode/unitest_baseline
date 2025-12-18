"""
QUESTION:
Implement a recursive function `reverse_linked_list` that takes the head node of a linked list and reverses the list in-place. The function should have a time complexity of O(n) and space complexity of O(1), where n is the number of nodes in the linked list. The function should not use the built-in reverse() function, additional variables, or data structures other than the input linked list itself. The linked list nodes can contain objects or strings as data, and the function should be able to handle these cases.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(node, prev=None):
    if node is None:
        return prev
    next_node = node.next
    node.next = prev
    return reverse_linked_list(next_node, node)