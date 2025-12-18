"""
QUESTION:
Implement a function named `get_nth_from_end` that takes the head of a linked list and an integer `n` as input, and returns the value of the nth element from the end of the linked list. The linked list is guaranteed to have at least `n` elements and cannot be modified. Do not use any built-in methods or functions for accessing the elements of the linked list.
"""

def get_nth_from_end(head, n):
    p1 = head
    p2 = head

    # Move p2 n steps ahead
    for _ in range(n):
        p2 = p2.next

    # If p2 becomes null, return the value at head
    if p2 is None:
        return p1.value

    # Move both p1 and p2 one step at a time until p2 reaches the end
    while p2.next is not None:
        p1 = p1.next
        p2 = p2.next

    # Return the value at p1
    return p1.value