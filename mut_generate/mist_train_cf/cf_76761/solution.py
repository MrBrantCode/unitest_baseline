"""
QUESTION:
Write a function named `level_info` that takes the root node of a binary tree as input. Each node in the binary tree has a value and a color, which can be either 'red' or 'blue'. The function should return a list of dictionaries, where each dictionary represents a level in the binary tree. The dictionary for each level should contain the level number, the total number of nodes at that level, and the number of nodes with 'red' and 'blue' colors at that level.
"""

from collections import deque

class TreeNode:
    def __init__(self, value, color, left=None, right=None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right

def level_info(root):
    result = []
    queue = deque([(root, 0)])
    
    while queue:
        node, level = queue.popleft()
        if node:
            if len(result) == level:
                result.append({'level': level, 'total': 0, 'red': 0, 'blue': 0})
            result[level]['total'] += 1
            result[level][node.color] += 1
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    
    return result