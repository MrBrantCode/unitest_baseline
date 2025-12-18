"""
QUESTION:
Implement a function `zigzag` that prints the elements of a ternary tree in a zig-zag order. The `zigzag` function takes as input the root of the ternary tree and prints the elements level by level, alternating between left-to-right and right-to-left order. Assume a given `TreeNode` class with attributes `val`, `left`, `mid`, and `right`.
"""

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.mid = None
        self.right = None

def zigzag(root):
    if root is None:
        return

    deq = deque([(root, 0)])
    is_left_to_right = True

    while deq:
        len_deq = len(deq)

        for i in range(len_deq):
            curr_node, level = deq.popleft() if is_left_to_right else deq.pop()

            print(curr_node.val, end=' ')

            children = [curr_node.left, curr_node.mid, curr_node.right]
            children = [node for node in children if node is not None]
            
            if is_left_to_right:
                deq.extend([(node, level + 1) for node in children])
            else:
                for node in children[::-1]:
                    deq.appendleft((node, level + 1))
        
        print()
        is_left_to_right = not is_left_to_right