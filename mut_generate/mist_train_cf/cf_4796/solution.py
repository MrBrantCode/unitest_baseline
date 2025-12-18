"""
QUESTION:
Implement the `reverseList` function to reverse a singly-linked list in-place without creating any new nodes or using any additional data structures. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list. The implementation should handle edge cases where the linked list is empty or only contains one node.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev