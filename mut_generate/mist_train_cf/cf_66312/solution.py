"""
QUESTION:
Design a Binary Search Tree class where each node contains a 2D point (x, y) with the following requirements: 

- The tree should be ordered based on the x-coordinate of the points. If two points have the same x-coordinate, they should be ordered based on their y-coordinate. 
- The class should have an `insert` function to add new points into the tree. 
- The tree should not contain duplicate points. If a duplicate point is inserted, it should be handled accordingly.
"""

class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

def entrance(point, current_node=None):
    if current_node is None:
        return Node(point)
    if point[0] < current_node.point[0]:  
        current_node.left = entrance(point, current_node.left)
    elif point[0] > current_node.point[0]:  
        current_node.right = entrance(point, current_node.right)
    else:
        if point[1] < current_node.point[1]:  
            current_node.left = entrance(point, current_node.left)
        elif point[1] > current_node.point[1]:  
            current_node.right = entrance(point, current_node.right)
        else:
            return current_node  # handle duplicate points
    return current_node