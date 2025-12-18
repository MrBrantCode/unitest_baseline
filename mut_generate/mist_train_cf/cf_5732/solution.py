"""
QUESTION:
Write a function called `reverseList` that takes the head of a linked list as its input, reverses the order of its elements using only recursion, and returns the head of the reversed list. The function should have a space complexity of O(1) and should not use any additional data structures.
"""

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def reverseList(head):
    # Base case: if the current node is None or the last node, return it as the new head
    if head is None or head.next is None:
        return head
    
    # Recursively reverse the rest of the list
    reversed_head = reverseList(head.next)

    # Change the next pointer of the next node to point to the current node
    head.next.next = head
    
    # Set the next pointer of the current node to None
    head.next = None

    # Return the new head of the reversed list
    return reversed_head