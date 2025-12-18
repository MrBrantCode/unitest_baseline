"""
QUESTION:
Implement a function `swap_positions` that takes the head of a singly linked list and two 1-based index positions as input, and swaps the nodes at the specified positions in the list in-place. The function should return the modified linked list.

The function should handle the following restrictions:

- If either of the specified positions is invalid or out of range, return the original linked list without making any changes.
- The swap operation should modify the original linked list in-place, without creating a new linked list or using any additional data structures.
- The node values can be of any data type.
- The linked list can have duplicate values, and the swap operation should handle them correctly.
- If the specified positions are the same, no swap should be performed and the linked list should remain unchanged.
- The time complexity of the solution should be O(n), where n is the number of nodes in the linked list.
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