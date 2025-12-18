"""
QUESTION:
Implement a function named `swapNodes` that takes the head of a linked list and two positions `pos1` and `pos2` as input, and returns the head of the updated linked list after swapping the nodes at the specified positions. The function should handle the case when the positions are 1 and the nodes are adjacent. The positions are 1-indexed. The function should assume that the positions are valid and within the range of the list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head, pos1, pos2):
    # Create a dummy node and set its next pointer to the head
    dummy = ListNode(0)
    dummy.next = head

    # Find the nodes at the specified positions
    prev1, prev2 = dummy, dummy
    for _ in range(pos1-1):
        prev1 = prev1.next
    for _ in range(pos2-1):
        prev2 = prev2.next
    
    # Swap the next pointers of the nodes
    node1 = prev1.next
    node2 = prev2.next
    prev1.next = node2
    prev2.next = node1
    node1.next, node2.next = node2.next, node1.next

    # Return the updated head of the linked list
    return dummy.next