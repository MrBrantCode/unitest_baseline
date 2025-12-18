"""
QUESTION:
Implement a function `reverseList(head)` that takes the head of a singly-linked list as input and returns the head of the reversed linked list. The linked list is defined as a class `ListNode` where each node has a value `val` and a pointer to the next node `next`. The function should handle cases where the input linked list is empty or contains only one node.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    # if the linked list is empty or only contains one node
    if not head or not head.next:
        return head
    
    # initialize three pointers to keep track of the previous, current and next nodes
    prev = None
    curr = head
    
    # traverse through the linked list
    while curr:
        # store the next node
        next_node = curr.next
        # reverse the direction of the current node
        curr.next = prev
        # move the pointers to the next nodes
        prev = curr
        curr = next_node
    
    # return the new head of the reversed linked list
    return prev