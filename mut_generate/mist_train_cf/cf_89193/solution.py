"""
QUESTION:
Write a function `traverse_bst` that traverses a binary search tree using a non-recursive depth-first search algorithm and prints the values of nodes in ascending order along with their respective levels. The function should also calculate and print the average value of nodes at each level. 

The function should take as input the root node of the binary search tree and should not return any value. The binary search tree nodes should be represented using a `Node` class with `value`, `left`, and `right` attributes.

The function should use a level-order traversal approach to minimize memory usage and should handle the case where the input tree is empty.
"""

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse_bst(root):
    if not root:
        return
    
    # Initialize the queue for level-order traversal
    queue = deque()
    queue.append((root, 0))  # Tuple with node and level
    
    # Initialize variables for average calculation
    level_sum = 0
    level_count = 0
    current_level = 0

    while queue:
        node, level = queue.popleft()

        # Check if we have moved to a new level
        if level != current_level:
            # Calculate and print the average value for the previous level
            if level_count > 0:
                average = level_sum / level_count
                print(f"Level {current_level}: Average = {average}")

            # Reset variables for the new level
            level_sum = 0
            level_count = 0
            current_level = level

        # Process the current node
        level_sum += node.value
        level_count += 1
        print(f"Level {level}: Node = {node.value}")

        # Add the left and right children to the queue
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    # Print the average value for the last level
    if level_count > 0:
        average = level_sum / level_count
        print(f"Level {current_level}: Average = {average}")