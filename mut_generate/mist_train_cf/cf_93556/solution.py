"""
QUESTION:
Implement a function `get_nth_from_end(head, n)` that returns the value of the nth element from the end of a linked list, where `head` is the head of the linked list and `n` is the position of the element from the end. The linked list is guaranteed to have at least n elements and its structure cannot be modified.
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