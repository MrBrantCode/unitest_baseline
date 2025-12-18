"""
QUESTION:
Implement a function called `removeDuplicates` that takes the head of a linked list as input, removes duplicates from the list, and returns the head of the new linked list. The function should have a time complexity of O(n), where n is the number of nodes in the linked list, and should not use any additional data structures. The linked list nodes contain integer values, and the function should preserve the original order of the nodes in the resulting linked list. The function should not modify the original linked list, but instead create a new linked list with the non-duplicate nodes.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def removeDuplicates(head):
    if not head or not head.next:
        return head

    current = head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head