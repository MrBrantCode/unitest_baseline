"""
QUESTION:
Write a function `find_kth_from_end(head, k)` that takes the head of a linked list and an integer `k` as input, where `k` is a positive integer less than or equal to the length of the list, and returns the value of the `k`-th element from the end of the list. If the length of the list is odd, return the middle element; if the length of the list is even, return the second middle element.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_kth_from_end(head, k):
    slow = head
    fast = head
    count = 0
    
    while fast.next:
        fast = fast.next
        count += 1
        if count > k:
            slow = slow.next
    
    return slow.val