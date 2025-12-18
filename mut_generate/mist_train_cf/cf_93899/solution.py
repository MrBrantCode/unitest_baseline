"""
QUESTION:
Implement a function `postorder_sum` that takes the root of a binary tree as input and returns the sum of all the values in the tree, traversing the tree in post-order. The function should not use recursion, any additional data structures, or modify the original tree structure. The function should assume that the binary tree is defined using a `TreeNode` class with `value`, `left`, and `right` attributes.
"""

def postorder_sum(root):
    if root is None:
        return 0

    stack = []
    current = root
    sum = 0

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            temp = stack[-1].right
            if temp is None:
                temp = stack.pop()
                sum += temp.value

                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    sum += temp.value
            else:
                current = temp
        else:
            break

    return sum