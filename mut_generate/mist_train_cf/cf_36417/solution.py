"""
QUESTION:
Implement the `postorder` method within the `Solution` class to perform a postorder traversal on the given N-ary tree and return the values of the nodes in the traversal order. 

The N-ary tree is represented using a list of nodes, where each node is a dictionary with a `val` key representing the node's value and a `children` key representing a list of the node's children.
"""

def postorder(root):
    if not root:
        return []
    
    result = []
    for child in root["children"]:
        result.extend(postorder(child))
    result.append(root["val"])
    
    return result