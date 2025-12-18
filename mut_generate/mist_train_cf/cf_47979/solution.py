"""
QUESTION:
Write a function named `count_nodes` that takes the head of a circular linked list as input and returns the number of nodes in the list. The function should not assume the presence of any sentinel node (like NULL) to signal the end of the list. The circular linked list is represented by a class `Node` with `data` and `next` attributes.
"""

def count_nodes(head):
    if head is None:
        return 0

    count = 1  # start counting from the head node
    current = head.next

    while current != head:
        count += 1
        current = current.next

    return count