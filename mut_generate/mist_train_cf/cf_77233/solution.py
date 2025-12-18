"""
QUESTION:
Create a function `mergeTrees(tree1, tree2)` that merges two disjoint binary search trees with unique elements into a balanced binary search tree, without using any extra space. The function should return the root of the merged binary search tree.
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def size(node):
  if node is None:
    return 0
  else:
    return(size(node.left) + 1 + size(node.right))

def insert(node, data):
  if node is None:
    return Node(data)
  else:
    if node.data > data:
      node.left = insert(node.left, data)
    else:
      node.right = insert(node.right, data)
  return node

def inorderTraversal(node, inorder):
  if node is None:
    return
  inorderTraversal(node.left, inorder)
  inorder.append(node.data)
  inorderTraversal(node.right, inorder)

def sortedArrayToBST(arr):
  if not arr:
    return None
  mid = len(arr) // 2
  root = Node(arr[mid])
  root.left = sortedArrayToBST(arr[:mid])
  root.right = sortedArrayToBST(arr[mid+1:])
  return root

def mergeTrees(tree1, tree2):
  if size(tree1) < size(tree2):
    tree1, tree2 = tree2, tree1
  inorder = []
  inorderTraversal(tree1, inorder)
  inorderTraversal(tree2, inorder)
  sortedArr = sorted(inorder)
  return sortedArrayToBST(sortedArr)