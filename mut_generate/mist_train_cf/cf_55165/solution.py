"""
QUESTION:
Design a method `rotate` that takes an integer `N` as input and rotates a doubly linked list by N nodes. The method should adjust the relevant pointers in the list to complete the rotation. The input list is a doubly linked list and N is a non-negative integer. The method should return the rotated list without modifying the original list structure. The rotation should be performed in a clockwise direction.
"""

def rotate(self, N):
    if not self.head or N <= 0:
        return

    current = self.head
    count = 1

    while count < N and current is not None:
        current = current.next_node
        count += 1
    if current is None: 
        return
        
    Nth_node = current
    while current.next_node is not None:
        current = current.next_node

    current.next_node = self.head
    self.head.prev_node = current

    self.head = Nth_node.next_node
    self.head.prev_node = None

    Nth_node.next_node = None