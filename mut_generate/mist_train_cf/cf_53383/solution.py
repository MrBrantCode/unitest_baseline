"""
QUESTION:
Write a function `clone(start)` that clones a complex doubly linked list where each node has two pointers, one to the next node and another to a random node in the list. The function should take the start node of the original list as input and return the head node of the cloned list. The cloned list should maintain the same structure as the original list, with each node's next and random pointers pointing to the correct nodes in the cloned list.
"""

class Node: 
    def __init__(self, data, next=None, random=None): 
        self.data = data 
        self.next = next
        self.random = random 

def clone(start):
    node_dict = dict()

    def clone_recursion(node):
        if node is None:
            return None
        if node in node_dict:
            return node_dict[node]
        else:
            cloned = Node(node.data)
            node_dict[node] = cloned
            cloned.next = clone_recursion(node.next)
            cloned.random = clone_recursion(node.random)
            return cloned

    return clone_recursion(start)