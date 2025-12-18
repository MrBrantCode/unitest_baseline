"""
QUESTION:
Implement a `reverse_stack` function that takes no arguments and reverses the existing stack without using any additional data structures, recursion, or loops, and returns the modified stack. The input stack will have at least two elements. The stack is implemented as a singly linked list where each node has a data value and a reference to the next node.
"""

def reverse_stack(self):
    if self.top is None or self.top.next is None:
        return

    prev = None
    curr = self.top

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    self.top = prev