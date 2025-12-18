"""
QUESTION:
Write a function called `mergeTrees` that merges two unbalanced binary search trees into a self-balancing binary search tree. The function should take as input two tree roots `root1` and `root2` and return the root of the merged tree. The merged tree should be a binary search tree where the difference in height between the left and right subtrees of every node is at most 1. The time complexity of the merge operation should be O(N log N) and the space complexity should be O(N), where N is the total number of nodes in the input trees.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def inOrder(root, sorted_list):
    if not root:
        return
    inOrder(root.left, sorted_list)
    sorted_list.append(root.key)
    inOrder(root.right, sorted_list)

def sortedListToBST(sorted_list):
    if not sorted_list:
        return None

    mid = len(sorted_list) // 2
    root = Node(sorted_list[mid])
    root.left = sortedListToBST(sorted_list[:mid])
    root.right = sortedListToBST(sorted_list[mid+1:])
    root.height = max(getHeight(root.left),
                      getHeight(root.right)) + 1

    return root

def getHeight(root):
    if root == None:
        return 0
    return root.height

def mergeTrees(root1, root2):
    sorted_list1 = []
    sorted_list2 = []
    inOrder(root1, sorted_list1)
    inOrder(root2, sorted_list2)
    merged_sorted_list = sorted_list1 + sorted_list2
    merged_sorted_list.sort()

    return sortedListToBST(merged_sorted_list)