"""
QUESTION:
Create a function `reverse_list` that reverses a singly linked list recursively with a time complexity of O(n) and a space complexity not exceeding O(n). The function should update the next pointers of the nodes accordingly.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_list(head):
    def reverse(current_node, previous_node):
        if current_node is None:
            return previous_node
        next_node = current_node.next
        current_node.next = previous_node
        return reverse(next_node, current_node)
    return reverse(head, None)