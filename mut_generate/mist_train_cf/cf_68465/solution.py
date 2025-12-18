"""
QUESTION:
Create a function named `verifyAndGeneratePostorder` that takes as input an array of unique integers `preorder` representing the preorder traversal sequence of a binary search tree. Return a tuple containing a boolean indicating whether the input array is a valid preorder traversal sequence of a binary search tree and the postorder traversal sequence of the same tree. The input array is guaranteed to contain at least 1 and at most 10^4 elements, each in the range [1, 10^4].
"""

def verifyAndGeneratePostorder(preorder):
    root = float('-inf')
    stack = []
    postorder = []

    def generatePostOrder(preorder):
        if not preorder: return []
        root = preorder[0]
        i = next((i for i, val in enumerate(preorder) if val > root), len(preorder))
        return generatePostOrder(preorder[1:i]) + generatePostOrder(preorder[i:]) + [root]

    for value in preorder:
        if value < root:
            return False, []
        while stack and stack[-1] < value:
            root = stack.pop()
        stack.append(value)
    postorder = generatePostOrder(preorder)
    return True, postorder