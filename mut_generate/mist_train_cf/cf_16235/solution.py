"""
QUESTION:
Remove elements from a singly linked list of integers that have a greater value than a given number X and return the modified linked list. If the linked list is empty or X is greater than the maximum value in the linked list, return an empty linked list.

The function should be named removeElementsGreaterThanX and should have a time complexity of O(n), where n is the number of nodes in the linked list. It should not use any additional data structures and should not modify the original linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElementsGreaterThanX(head, X):
    """
    Removes elements from a singly linked list of integers that have a greater value than a given number X.
    
    Args:
    head (ListNode): The head of the linked list.
    X (int): The given number.

    Returns:
    ListNode: The head of the modified linked list.
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next:
        if prev.next.val > X:
            prev.next = prev.next.next
        else:
            prev = prev.next

    return dummy.next