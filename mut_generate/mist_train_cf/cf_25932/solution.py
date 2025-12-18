"""
QUESTION:
Write a function `delete_every_third_node` that deletes every third element of a given linked list. The function should take the head of the linked list as input and return the head of the modified linked list. The linked list nodes are assumed to have `data` and `next` attributes.
"""

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def delete_every_third_node(head):
    """
    Deletes every third element of a given linked list.

    Args:
        head (ListNode): The head of the linked list.

    Returns:
        ListNode: The head of the modified linked list.
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    count = 0
    
    while current.next and current.next.next:
        current = current.next
        count += 1
        if count == 2:
            current.next = current.next.next
            count = 0
    
    return dummy.next