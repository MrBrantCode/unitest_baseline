"""
QUESTION:
Write a function `reverseKGroup(head, k)` that reverses the nodes of a linked list `k` at a time and returns its modified list. The function should have a time complexity of O(n) and a space complexity of O(1), where `n` is the number of nodes in the linked list. The `head` is the head of the linked list and `k` is the number of nodes to be reversed together.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # Check if the linked list has at least k nodes
    count = 0
    curr = head
    while curr and count < k:
        curr = curr.next
        count += 1
    if count < k:
        return head
    
    # Reverse the group of k nodes
    prev = None
    curr = head
    for _ in range(k):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    # Connect the reversed group with the previous group
    head.next = reverseKGroup(curr, k)
    
    return prev