"""
QUESTION:
Implement a function called `deleteOccurrences(head, k)` that takes the head of a singly linked list and a key `k` as input, and returns the modified linked list with all occurrences of `k` deleted. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def deleteOccurrences(head, k):
    # Handle case where the first few nodes contain k
    while head is not None and head.value == k:
        head = head.next

    prev = None
    curr = head

    while curr is not None:
        if curr.value == k:
            if prev is not None:
                prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return head