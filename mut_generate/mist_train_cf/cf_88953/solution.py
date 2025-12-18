"""
QUESTION:
Write a function `swap_positions(head, pos1, pos2)` that swaps the nodes at positions `pos1` and `pos2` in a singly linked list, where `head` is the head of the linked list. The positions are 1-based index positions. If either of the specified positions is invalid or out of range, the function should return the original linked list without making any changes. The swap operation should modify the original linked list in-place, without creating a new linked list or using any additional data structures.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swap_positions(head, pos1, pos2):
    if pos1 == pos2:
        return head

    # Find the nodes at the specified positions
    current = head
    prev1 = None
    prev2 = None
    node1 = None
    node2 = None
    position = 1

    while current is not None:
        if position == pos1:
            node1 = current
        elif position == pos2:
            node2 = current

        if node1 is None:
            prev1 = current
        if node2 is None:
            prev2 = current

        current = current.next
        position += 1

    # Check if both nodes are found
    if node1 is None or node2 is None:
        return head

    # Adjust the next pointers to perform the swap
    if prev1 is None:
        head = node2
    else:
        prev1.next = node2

    if prev2 is None:
        head = node1
    else:
        prev2.next = node1

    node1.next, node2.next = node2.next, node1.next

    return head