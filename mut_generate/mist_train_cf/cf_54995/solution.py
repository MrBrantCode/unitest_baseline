"""
QUESTION:
Design a function named `sortedListToBST` that transforms a sorted linked list into a balanced binary search tree (BST). The function should take a linked list as input and return the root of the constructed BST. The function should handle a linked list of any size and be efficient in terms of both time and space complexity.
"""

class LNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def countNodes(head):
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count += 1
    return count

def sortedListToBSTRecur(head, n):
    if n <= 0:
        return None, head

    left, head = sortedListToBSTRecur(head, n // 2)

    root = TNode(head.val)
    root.left = left

    head = head.next
    
    root.right, head = sortedListToBSTRecur(head, n - n // 2 - 1)

    return root, head


def sortedListToBST(head):
    n = countNodes(head)
    return sortedListToBSTRecur(head, n)[0]