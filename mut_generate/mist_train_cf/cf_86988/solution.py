"""
QUESTION:
Implement the function `removeNodeAtPosition` that takes in the head pointer of a singly linked list and the position of the node to be removed. The position is 1-based, meaning the first node is at position 1, the second node is at position 2, and so on. The function should return the head pointer of the modified linked list. 

The linked list has at least one node and at most 10^3 nodes, each with a distinct positive integer value not exceeding 10^3. The position given is always valid, a positive integer less than or equal to the number of nodes in the linked list. The solution must have a time complexity of O(n), where n is the number of nodes in the linked list, and recursion is not allowed.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNodeAtPosition(head, position):
    if position == 1:
        head = head.next
        return head

    count = 1
    current = head
    while count < position - 1:
        count += 1
        current = current.next

    current.next = current.next.next

    return head