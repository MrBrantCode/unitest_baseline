"""
QUESTION:
Write a function `find_nth_from_end` that takes a linked list and an integer `n` as input, and returns the `n`th node from the end, its previous node, and a boolean indicating whether the `n`th node is the middle node of the list. The function should handle edge cases where the linked list is empty, has only one node, or has fewer than `n` nodes. The time complexity should be O(n) and the space complexity should be O(1).
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def find_nth_from_end(head, n):
    """
    This function finds the nth node from the end of a linked list, 
    its previous node, and checks if the nth node is the middle node.
    
    Args:
    head (Node): The head of the linked list.
    n (int): The position of the node from the end.
    
    Returns:
    tuple: A tuple containing the nth node's data, its previous node's data (or None if it's the head), 
           and a boolean indicating whether the nth node is the middle node.
    """
    runner = head
    nthNode = head
    previous_node = None
    
    # Move the runner n steps ahead
    for _ in range(n):
        if runner is None:
            return (None, None, False)  # return instead of print
        runner = runner.next

    # Move both pointers until the runner reaches the end
    while runner:
        runner = runner.next
        previous_node = nthNode
        nthNode = nthNode.next

    # Calculate the size of the linked list
    size = 0
    node = head
    while node:
        node = node.next
        size += 1

    # Check if the nth node is the middle node
    is_middle = size // 2 == n and size % 2 != 0 or size // 2 - 1 == n and size % 2 == 0

    return (nthNode.data if nthNode else None, previous_node.data if previous_node else None, is_middle)