"""
QUESTION:
Create a function named `remove` to remove specified nodes from a linked list using recursion. The function should take two parameters: `value` (the value of the node to be removed) and `node` (the current node in the recursion, defaults to the head of the linked list if not provided). The function should handle mutable and immutable node removals and edge cases where the node to be removed is the first or last node in the list.
"""

def remove(self, value, node=None):
    if node is None:
        node = self.head  # default to head node if node is None

    if node is None:
        return None

    if node.value == value:  # if the current node's value is the target value
        return node.next  # skip this node by pointing to the next node
    else:
        node.next = self.remove(value, node.next)  # keep looking

    return node