"""
QUESTION:
Write a function `find_kth_to_last(head, k)` that takes the head of a singly linked list and an integer `k` as input, and returns the value of the kth to last node. The time complexity of the solution should be O(n) and the space complexity should be O(1), where n is the number of nodes in the linked list. Assume k will always be valid (1 <= k <= length of the linked list) and k is a prime number.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_kth_to_last(head, k):
    p1 = p2 = head

    # Move p2 k-1 steps ahead
    for _ in range(k-1):
        p2 = p2.next

    # Move both pointers until p2 reaches the end of the linked list
    while p2.next is not None:
        p1 = p1.next
        p2 = p2.next

    return p1.val