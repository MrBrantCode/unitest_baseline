"""
QUESTION:
Write a function `calculate_sum` that takes the root of a binary tree as input, calculates the sum of all its nodes, and returns the sum along with the maximum and minimum values present in the tree. Additionally, the function should find and return the number of nodes that have a value greater than the average value of all nodes in the tree. The binary tree nodes contain positive integers and negative integers.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def calculate_sum(root):
    if root is None:
        return 0, float('-inf'), float('inf'), 0

    sum_val, max_val, min_val, count = root.value, root.value, root.value, 0
    stack, nodes = [(root, False)], [root.value]
    
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                if node.value > (sum_val / len(nodes)):
                    count += 1
            else:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                    nodes.append(node.left.value)
                    sum_val += node.left.value
                    max_val = max(max_val, node.left.value)
                    min_val = min(min_val, node.left.value)
                if node.right:
                    stack.append((node.right, False))
                    nodes.append(node.right.value)
                    sum_val += node.right.value
                    max_val = max(max_val, node.right.value)
                    min_val = min(min_val, node.right.value)

    return sum_val, max_val, min_val, count