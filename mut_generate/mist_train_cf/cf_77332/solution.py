"""
QUESTION:
Implement a function `sum_linkedlist(node)` that calculates the sum of all numbers in a singly linked list. The linked list is represented by instances of a class named Node, each holding a numerical value and a reference to the next node. The function should take the head of the linked list as input and return the sum of all node values. The linked list nodes are defined by the class `Node` with `val` and `next` attributes.
"""

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def sum_linkedlist(node):
    """
    Calculate the sum of all numbers in a singly linked list.

    Args:
    node (Node): The head of the linked list.

    Returns:
    int: The sum of all node values.
    """
    current = node
    total = 0
    while current is not None:
        total += current.val
        current = current.next
    return total