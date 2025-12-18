"""
QUESTION:
Delete a node from a circular linked list sorted in ascending order. The function should be able to delete the head or tail of the linked list. 

The function should have a time complexity of O(n), where n is the number of nodes in the linked list. However, if the node to delete is given (not the value), then it is possible to delete the node in O(1) time complexity. The function should only use constant extra space, i.e., no additional data structures should be used. The function should handle cases where the linked list is empty or contains only one node.

Function name: deleteNode 
Input: The head of the circular linked list and the value of the node to delete.
Output: The head of the modified circular linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNode(head, value):
    if head is None:
        return

    current = head
    prev = None
    while True:
        if current.data == value:
            if current == head:
                temp = head
                while temp.next != head:
                    temp = temp.next
                temp.next = head.next
                head = head.next
            elif current.next == head:
                prev.next = head
            else:
                prev.next = current.next
            return head
        prev = current
        current = current.next
        if current == head:
            break
    return head