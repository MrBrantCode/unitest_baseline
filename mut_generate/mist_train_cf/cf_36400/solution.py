"""
QUESTION:
Construct a binary tree from a given list of integers where `None` values are used to indicate the absence of a left or right child. Implement the `construct_binary_tree(nums)` function that takes the list of integers `nums` as input and constructs a binary tree. The function should return the root node of the constructed binary tree.

The input list `nums` represents a binary tree in level order, where the parent node is always before its children. If a node is `None`, its left and right children are not included in the list. The function should handle an empty input list, in which case it should return `None`. 

For example, given the input `nums = [3, 9, 20, None, None, 15, 7]`, the constructed binary tree should have the structure:

```
    3
   / \
  9  20
    /  \
   15   7
```
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree(nums):
    if not nums:
        return None

    nodes = [None if val is None else TreeNode(val) for val in nums]
    root = nodes[0]
    queue = [root]
    i = 1

    while queue and i < len(nums):
        node = queue.pop(0)
        if node:
            node.left = nodes[i]
            queue.append(node.left)
            i += 1
            if i < len(nums):
                node.right = nodes[i]
                queue.append(node.right)
                i += 1

    return root