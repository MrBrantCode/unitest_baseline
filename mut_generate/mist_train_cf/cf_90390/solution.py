"""
QUESTION:
Design an algorithm for a function named `reverse_list_iteratively(head, k)` that takes the head node of a singly linked list and an integer k as input. The function should reverse the linked list in-place, in groups of size k, using an iterative approach without using any extra space other than a few constant variables. The function should return the new head node of the reversed linked list. The time complexity of the algorithm should be O(n), where n is the number of nodes in the linked list.
"""

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list_iteratively(head, k):
    prev = None
    curr = head
    next = None
    count = 0
    
    while curr is not None and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1

    if next is not None:
        head.next = reverse_list_iteratively(next, k)

    return prev