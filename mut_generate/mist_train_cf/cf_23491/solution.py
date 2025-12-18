"""
QUESTION:
Design a function named `convertTernaryTreeToDoublyLinkedList` that converts a ternary tree to a doubly linked list. The function takes the root of the ternary tree as input and returns the head of the doubly linked list. The conversion should be done in a way that the left subtree of the root node is on the left side of the root in the linked list, the root node is in the middle, and the right subtree of the root node is on the right side of the root in the linked list. Each node in the linked list should have `val`, `next`, and `prev` attributes.
"""

class Node:
    def __init__(self, val, left=None, right=None, next=None, prev=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        self.prev = prev

def convertTernaryTreeToDoublyLinkedList(root):
    if root is None:
        return None

    left_head = convertTernaryTreeToDoublyLinkedList(root.left)
    right_head = convertTernaryTreeToDoublyLinkedList(root.right)

    if left_head is None and right_head is None:
        root.left = root.right = root.prev = root.next = None
        return root

    if left_head is None:
        root.prev = None
        root.next = right_head
        right_head.prev = root
        return root

    if right_head is None:
        root.next = None
        root.prev = left_head
        left_head.next = root
        while left_head.prev:
            left_head = left_head.prev
        return left_head

    while left_head.next:
        left_head = left_head.next

    left_head.next = root
    root.prev = left_head
    root.next = right_head
    right_head.prev = root
    while left_head.prev:
        left_head = left_head.prev
    return left_head