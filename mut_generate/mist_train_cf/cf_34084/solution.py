"""
QUESTION:
Implement the `RotateLinkedList` function to rotate a singly linked list to the right by a given number of places. The function should take the head of the linked list and a positive integer `k` as input and return the head of the rotated linked list. The last `k` nodes of the linked list should be moved to the front, and the rest of the elements should move to the right. If `k` is greater than the length of the linked list, it should be adjusted to be within the length of the linked list.
"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def RotateLinkedList(head, k):
    if not head or k == 0:
        return head

    # Calculate the length of the linked list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Adjust k to be within the length of the linked list
    k = k % length

    if k == 0:
        return head

    # Find the new head and tail after rotation
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    # Perform the rotation
    new_tail.next = None
    tail.next = head

    return new_head