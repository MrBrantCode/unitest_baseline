"""
QUESTION:
Create a function `serialize(root)` that converts a binary tree into a string representation, and another function `deserialize(data)` that reconstructs the binary tree from the string representation. The serialized string should represent each node by its value, and null nodes by "#". The functions should be able to handle any binary tree. 

Restrictions: 
- The `serialize(root)` function should return a string. 
- The `deserialize(data)` function should return the root node of the reconstructed binary tree.
- The time complexity of both functions should be O(n), where n is the number of nodes in the binary tree. 
- The space complexity of both functions should be O(n).
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def serialize(root):
    if root is None:
        return "#"
    
    result = str(root.val) + ","
    result += serialize(root.left) + ","
    result += serialize(root.right)
    
    return result

def deserialize(data):
    values = data.split(",")
    index = 0
    
    def deserializeHelper():
        nonlocal index
        
        if values[index] == "#":
            index += 1
            return None
        
        node = TreeNode(int(values[index]))
        index += 1
        node.left = deserializeHelper()
        node.right = deserializeHelper()
        
        return node
    
    return deserializeHelper()