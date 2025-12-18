"""
QUESTION:
Design a function `sortedListToBST` that converts a sorted linked list into a balanced binary search tree (BST). The function should handle nested linked lists and convert them into nested BSTs, manage a mix of linked lists and other data types within the same BST, and handle linked lists with nodes that are also linked lists. The function should be able to handle any level of nesting and linked lists of any size, including those containing recursive references. The function should return the root of the BST and its height, and handle duplicate values in the linked list according to BST rules.

The input is a linked list where each node is an instance of the `ListNode` class, defined as `class ListNode: def __init__(self, x): self.val = x; self.next = None`. The output should be a binary search tree where each node is an instance of the `TreeNode` class, defined as `class TreeNode: def __init__(self, x): self.val = x; self.left = None; self.right = None`. The function should achieve this in an efficient manner, with a time complexity of O(nlogn) where n is the number of nodes in the linked list.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedListToBST(head):
    def findSize(head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next  
            c += 1
        return c

    def convert(l, r):
        nonlocal head
        if l > r:
            return None
        mid = (l + r) >> 1
        left = convert(l, mid - 1)
        node = TreeNode(head.val)   
        node.left = left
        head = head.next
        node.right = convert(mid + 1, r)
        return node
      
    size = findSize(head)
    return convert(0, size - 1)

def height(root): 
    if root is None: 
        return 0 
    else: 
        lheight = height(root.left) 
        rheight = height(root.right) 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1