"""
QUESTION:
Implement a function called `rotateLinkedList` that takes a linked list head and an integer k as input parameters. The function should rotate the linked list k positions to the right in-place and return the modified linked list after rotation. Assume k is a non-negative integer and the linked list is non-empty with at least two nodes, where each node has a `data` attribute and a `next` attribute.
"""

def rotateLinkedList(head, k):
    if k == 0:
        return head
    
    # Find the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # Calculate the number of rotations needed
    k = k % length
    
    if k == 0:
        return head
    
    # Find the kth node from the end
    fast = head
    slow = head
    for _ in range(k):
        fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # Rotate the linked list
    new_head = slow.next
    slow.next = None
    fast.next = head
    
    return new_head