"""
QUESTION:
Sort a singly linked list in ascending order. Implement a function called `sortList` that takes the head of the linked list as input and returns the head of the sorted linked list. The input linked list is unsorted and contains integer values.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    """
    Sorts a singly linked list in ascending order.

    Args:
    head (ListNode): The head of the linked list.

    Returns:
    ListNode: The head of the sorted linked list.
    """
    if not head or not head.next:
        return head

    # Find the middle of the linked list
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Split the linked list into two halves
    mid = slow.next
    slow.next = None

    # Recursively sort the two halves
    left = sortList(head)
    right = sortList(mid)

    # Merge the two sorted halves
    return merge(left, right)


def merge(l1, l2):
    """
    Merges two sorted linked lists into one sorted linked list.

    Args:
    l1 (ListNode): The head of the first linked list.
    l2 (ListNode): The head of the second linked list.

    Returns:
    ListNode: The head of the merged linked list.
    """
    if not l1:
        return l2
    elif not l2:
        return l1

    if l1.val < l2.val:
        l1.next = merge(l1.next, l2)
        return l1
    else:
        l2.next = merge(l1, l2.next)
        return l2