"""
ORIGINAL QUESTION:
Create a function `mergeTwoLists(l1, l2)` that takes two sorted linked lists `l1` and `l2` as input and returns a new sorted linked list containing all elements from both lists. The time complexity of the solution should be O(n+m), where n and m are the lengths of the two linked lists respectively.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    # Create a dummy node as the head of the merged list
    dummy = ListNode(0)
    # Pointer to the current node of the merged list
    curr = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # Append the remaining nodes of the other list
    curr.next = l1 or l2

    # Return the head of the merged list
    return dummy.next