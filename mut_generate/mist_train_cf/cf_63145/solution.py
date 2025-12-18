"""
QUESTION:
Construct a binary tree from given preorder and postorder traversals. The tree must be balanced. The values in the traversals `pre` and `post` are distinct positive integers and are permutations of `1, 2, ..., pre.length` where `1 <= pre.length == post.length <= 30`. If there exists multiple answers, you can return any of them. The function name should be `constructFromPrePost` and takes two parameters `pre` and `post`.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructFromPrePost(pre, post):
    if not pre:
        return None
    root = TreeNode(pre[0])
    if len(pre) == 1:
        return root
    L = post.index(pre[1]) + 1
    root.left = constructFromPrePost(pre[1:L+1], post[:L])
    root.right = constructFromPrePost(pre[L+1:], post[L:-1])
    return root