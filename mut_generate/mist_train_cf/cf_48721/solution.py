"""
QUESTION:
Write a function called `deleteDuplicates` that takes the head of a sorted linked list as input and returns the head of the modified linked list. The linked list should be modified in-place to remove all duplicate nodes while preserving the order of the remaining nodes. The input linked list is guaranteed to be sorted in ascending order and will contain between 0 and 1000 nodes, with node values in the range -1000 to 1000.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    if head is None:
        return head
    current = head
    while current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head