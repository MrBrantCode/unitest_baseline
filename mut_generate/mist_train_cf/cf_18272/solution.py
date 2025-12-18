"""
QUESTION:
Create a function `merge_sorted_lists` that takes two sorted linked lists as input and returns a new sorted linked list. The input linked lists may contain duplicate values. The merged list should be sorted in non-decreasing order with no duplicate values. The input linked lists are not modified.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    prev_val = None

    while l1 and l2:
        if l1.val < l2.val:
            if l1.val != prev_val:
                current.next = l1
                current = current.next
                prev_val = l1.val
            l1 = l1.next
        elif l2.val < l1.val:
            if l2.val != prev_val:
                current.next = l2
                current = current.next
                prev_val = l2.val
            l2 = l2.next
        else:
            if l1.val != prev_val:
                current.next = l1
                current = current.next
                prev_val = l1.val
            l1 = l1.next
            l2 = l2.next

    current.next = l1 if l1 else l2
    return dummy.next