"""
QUESTION:
Implement a function `reverse_doubly_linked_list` that takes the head of a doubly linked list as input, reverses the list in-place, and returns the new head. The function must have a time complexity of O(n) and cannot use any additional data structures or loops.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def reverse_doubly_linked_list(head):
    if not head or not head.next:
        return head
    
    def reverse_helper(curr):
        if not curr.next:
            # Update the new head to be the last node
            nonlocal head
            head = curr
            return

        # Reverse the remaining list starting from the next node
        reverse_helper(curr.next)

        # Swap the previous and next pointers of the current node
        curr.next.next = curr
        curr.prev = curr.next
        curr.next = None
    
    reverse_helper(head)
    
    # Reset the previous pointer of the new head to None
    head.prev = None
    
    return head