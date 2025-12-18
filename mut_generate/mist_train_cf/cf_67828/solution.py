"""
QUESTION:
Implement the `sortedListAdditionalOperations(head)` function to sort a singly linked list using insertion sort, reverse the sorted list, and return the middle node of the reversed list. The list may contain duplicate values; in such cases, return any one of the middle nodes.

The linked list is defined by a `ListNode` class with `val` and `next` attributes. The `head` node of the list is passed as an argument to the function.

Constraints: The number of nodes in the list is in the range `[1, 5000]` and `-5000 <= Node.val <= 5000`.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def sortedListAdditionalOperations(head):
    # Base case
    if head is None or head.next is None:
        return head

    # Initialize a new head node
    new_head = ListNode(0)
    new_head.next = head
    curr = head

    # Implement the Insertion Sort
    while curr is not None and curr.next is not None:
        if curr.val <= curr.next.val:
            curr = curr.next
        else:
            nxt = curr.next
            prev = new_head
            while prev.next.val < nxt.val:
                prev = prev.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

    # Reverse the sorted list
    prev = None
    curr = new_head.next
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head = prev

    # Find Mid node
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow