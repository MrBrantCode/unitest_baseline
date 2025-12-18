"""
QUESTION:
Given an integer `n`, return all the structurally unique binary search trees (BST's), which have exactly `n` nodes of unique values from `1` to `n`. Return the answer in any order.

Restrictions: 
- `1 <= n <= 8` 
- Note that the balance property is not guaranteed as it is not a property of BSTs.

Function name: `generateTrees(n)`
"""

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def generateTrees(n):
  def generate_trees(start, end):
      if start > end:
          return [None,]
      
      all_trees = []
      for i in range(start, end + 1):  
          left_trees = generate_trees(start, i - 1)
          right_trees = generate_trees(i + 1, end)
          
          for l in left_trees:
              for r in right_trees:
                  current_tree = TreeNode(i)
                  current_tree.left = l
                  current_tree.right = r
                  all_trees.append(current_tree)
      
      return all_trees
  
  return generate_trees(1, n) if n else []