"""
QUESTION:
Implement the function `sort_linked_list` to sort a single-linked list in ascending order. The function should take the head of the list as input and return the head of the sorted list. The list is unsorted, and each node has a unique integer value. The function should not use any additional data structures.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_linked_list(head):
    """
    Sorts a single-linked list in ascending order.
    
    Args:
    head (ListNode): The head of the list.
    
    Returns:
    ListNode: The head of the sorted list.
    """
    
    # Base case: If the list is empty or has one element, it is already sorted.
    if not head or not head.next:
        return head
    
    # Find the minimum value in the list.
    min_node = head
    current = head.next
    while current:
        if current.val < min_node.val:
            min_node = current
        current = current.next
    
    # If the minimum value is not the head, swap them.
    if min_node != head:
        head.val, min_node.val = min_node.val, head.val
    
    # Recursively sort the rest of the list.
    head.next = sort_linked_list(head.next)
    
    return head