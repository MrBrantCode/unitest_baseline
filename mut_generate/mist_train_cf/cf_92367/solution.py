"""
QUESTION:
Write a function `serialize(root)` to convert a binary tree into a string representation where each node is represented by its value and the null nodes are represented by '#'. The serialized string should be such that it can be deserialized back into the original binary tree. Also, implement a function `deserialize(data)` to deserialize the serialized string and construct the binary tree. 

The serialized string should be a comma-separated string where each node's value is represented by its value and null nodes are represented by '#'. The tree can be reconstructed from the serialized string using preorder traversal.
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