"""
QUESTION:
Construct a maximum binary tree from a given array of unique integers and calculate its height. The function `constructMaximumBinaryTree(nums)` should take an array `nums` as input, where `1 <= nums.length <= 1000` and `0 <= nums[i] <= 1000`, and return the root node of the constructed maximum binary tree. Additionally, implement the function `height(root)` to calculate the height of the constructed binary tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructMaximumBinaryTree(nums) -> 'TreeNode':
    if not nums:
        return None
    # Find the index of the maximum number
    max_index = nums.index(max(nums))
    # Create a root node
    root = TreeNode(nums[max_index])
    # Recursively build left and right subtree
    root.left = constructMaximumBinaryTree(nums[:max_index])
    root.right = constructMaximumBinaryTree(nums[max_index + 1:])
    return root

def height(root) -> int:
    if root is None:
        return 0
    else :
        # Compute the height of each subtree 
        left_height = height(root.left)
        right_height = height(root.right)

        # Use the larger one
        if left_height > right_height :
            return left_height+1
        else:
            return right_height+1