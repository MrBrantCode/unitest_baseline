"""
QUESTION:
Write a function `zigzagLevelOrder(root)` that takes the root of a non-empty complete binary tree as input and returns a list of lists representing the nodes of the binary tree in a zigzag level order traversal. The tree is represented as a list of lists, where each inner list contains the value of a node and the indices of its left and right children.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = [root]
    level = 0

    while queue:
        level_nodes = []
        next_level_node_count = 0
        for _ in range(len(queue)):
            node = queue.pop(0)
            if level % 2 == 0:
                level_nodes.append(node.value)
            else:
                level_nodes.insert(0, node.value)

            if node.left:
                queue.append(node.left)
                next_level_node_count += 1
            if node.right:
                queue.append(node.right)
                next_level_node_count += 1

        result.append(level_nodes)
        level += 1

    return result