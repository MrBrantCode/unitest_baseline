"""
QUESTION:
Create a function `reverse_list` that takes the head of a singly linked list as input and reverses the linked list recursively. The function should have a time complexity of O(n) and space complexity not exceeding O(n), where n is the number of nodes in the linked list. The function should also update the next pointers of the nodes accordingly.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_list(head):
    if head is None:
        return head

    def reverse(current_node, previous_node):
        if current_node.next is None:
            current_node.next = previous_node
            return current_node
        next_node = current_node.next
        current_node.next = previous_node
        return reverse(next_node, current_node)

    return reverse(head, None)