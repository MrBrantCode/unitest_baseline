"""
QUESTION:
Develop an efficient algorithm to find the middle element of a circular linked list with an odd number of nodes, without knowing the size of the list. The function should be named `get_middle_node` and take the head of the circular linked list as its input. The function should return the value of the middle node. Assume that the circular linked list is singly-linked and each node has a `value` and a `next` pointer.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_middle_node(head):
    tortoise = head
    hare = head
    prev_node = head

    while hare is not None and hare.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next
        if hare == tortoise:
            break
            
    tortoise = tortoise.next
    while tortoise != hare:
        prev_node = tortoise 
        tortoise = tortoise.next

    return prev_node.value