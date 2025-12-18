"""
QUESTION:
Implement the `sortLinkedList` function to sort a singly linked list in ascending order in-place. The input linked list is guaranteed to have at least two nodes, and each node contains an integer value. The solution must have a time complexity of O(n log n) and a space complexity of O(1).
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortLinkedList(head):
    if head.next is None:
        return head
    
    # Divide the linked list into two halves
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    second_half = slow.next
    slow.next = None
    
    # Recursively sort each half of the linked list
    first_half = sortLinkedList(head)
    second_half = sortLinkedList(second_half)
    
    # Merge the two sorted halves back together
    dummy = ListNode(0)
    curr = dummy
    
    while first_half and second_half:
        if first_half.val < second_half.val:
            curr.next = first_half
            first_half = first_half.next
        else:
            curr.next = second_half
            second_half = second_half.next
        curr = curr.next
    
    if first_half:
        curr.next = first_half
    if second_half:
        curr.next = second_half
    
    return dummy.next