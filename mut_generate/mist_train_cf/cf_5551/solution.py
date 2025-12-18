"""
QUESTION:
Write a function `rotateDoublyLinkedList` that takes the head of a doubly linked list and an integer `k` as input parameters. The function should rotate the doubly linked list `k` positions to the right and return the modified doubly linked list after rotation. Do not create a new doubly linked list. Modify the original doubly linked list in-place.

Constraints:
- `k` is a non-negative integer.
- The doubly linked list is non-empty and contains at least two nodes.
- The data in the doubly linked list nodes can be any valid Python object.
- The doubly linked list can contain duplicate elements.
- The doubly linked list can be of any length.

The doubly linked list node has the following structure:
```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
```
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

def rotateDoublyLinkedList(head, k):
    # Check if k is 0 or the linked list is empty
    if k == 0 or head is None:
        return head
    
    # Find the length of the linked list
    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1
    
    # If k is greater than the length, take the modulo to get the effective rotation count
    k = k % length
    
    # If k is 0 after taking modulo, no rotation is needed
    if k == 0:
        return head
    
    # Find the new tail node after rotation
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    
    # Update the connections
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    head.prev = tail
    new_head.prev = None
    
    return new_head