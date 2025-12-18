"""
QUESTION:
Implement a doubly linked list with two functions: `insert_at_head` and `remove_duplicates`. The `insert_at_head` function inserts a new node at the head of the list, ensuring the list remains sorted in ascending order, and handles cases where the new node's value is equal to an existing node's value by inserting it after the existing node. The `remove_duplicates` function removes any duplicate elements from the list. The implementation should have a time complexity of O(n), where n is the number of nodes in the list, and should not use any additional data structures such as arrays or sets.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def entrance(head, value):
    new_node = Node(value)

    if not head:
        return new_node

    # Handle case where new node value is less than head node's value
    if value <= head.data:
        new_node.next = head
        head.prev = new_node
        return new_node

    current = head
    while current.next:
        # Handle case where new node value is equal to an existing node's value
        if value == current.data:
            new_node.prev = current
            new_node.next = current.next
            current.next = new_node
            if new_node.next:
                new_node.next.prev = new_node
            return head

        if value <= current.next.data:
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
            new_node.next.prev = new_node
            return head

        current = current.next

    # Handle case where new node value is greater than any existing node's value
    new_node.prev = current
    current.next = new_node
    return head

def remove_duplicates(head):
    current = head

    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
            if current.next:
                current.next.prev = current
        else:
            current = current.next

    return head