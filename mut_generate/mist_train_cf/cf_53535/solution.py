"""
QUESTION:
Given the head of a hierarchical bidirectional linked list, where each node has a value, a pointer to its previous node, a pointer to its next node, and a child pointer to another node in the hierarchy, write a function `flatten` that takes the head of the hierarchical linked list as input and returns the head of the flattened list. The function should be able to handle up to 1000 nodes, with node values ranging from 1 to 10^5. The goal is to flatten the list such that all nodes are presented in a single-level bidirectional linked list.
"""

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head: 'Node') -> 'Node':
    if not head:
        return 
    
    pseudoHead = Node(0,None,head,None)
    prev = pseudoHead
    
    stack = []
    stack.append(head)
    
    while stack:
        curr = stack.pop()
        
        prev.next = curr
        curr.prev = prev
        
        if curr.next:
            stack.append(curr.next)
        
        if curr.child:
            stack.append(curr.child)
            curr.child = None
        
        prev = curr
    pseudoHead.next.prev = None
    return pseudoHead.next