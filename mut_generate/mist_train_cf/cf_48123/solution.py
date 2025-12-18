"""
QUESTION:
Write a function named `is_mirror` that checks if two binary trees are mirror images of each other. The function should take two binary tree roots `root1` and `root2` as input and return `True` if they are mirror images, and `False` otherwise. The function should consider both the structure and node values of the trees. Note that using threading is optional and may not necessarily improve performance due to Python's Global Interpreter Lock (GIL).
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def is_mirror(root1, root2):
  if root1 is None and root2 is None:
    return True
  if root1 is not None and root2 is not None:
    if root1.data == root2.data:
      return (is_mirror(root1.left, root2.right) and
              is_mirror(root1.right, root2.left))

  return False