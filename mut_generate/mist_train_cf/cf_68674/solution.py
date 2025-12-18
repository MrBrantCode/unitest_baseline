"""
QUESTION:
Create a method `clone_tree(root)` that clones a given N-ary tree and returns the root of the cloned tree. The method should also support a `locate_node(root, target)` operation that finds the node with a specified value in the cloned tree. 

In the N-ary tree, each node has a `val` (int), a list of its `offspring`, and a `parent` pointer. The tree's serialization is in level order traversal, with each cluster of offspring separated by a null value. The depth of the N-ary tree is less than or equal to `1000`, the total count of nodes is within the range `[0, 10^4]`, and the value of each node is unique.
"""

from collections import deque

class Node:
    def __init__(self, val: int = 0, offspring: 'list[Node]' = None):
        self.val = val
        self.offspring = offspring if offspring is not None else []
        self.parent = None # Parent not needed for this problem

def clone_tree(root):
    if root is None: return None
    clone_root = Node(root.val)
    clone_map = {root.val: clone_root}
    q = deque([(root, clone_root)])
    while q:
        node, clone_node = q.popleft()
        for child in node.offspring:
            if child.val not in clone_map:
                clone_child = Node(child.val)
                clone_map[child.val] = clone_child
                q.append((child, clone_child))
                clone_node.offspring.append(clone_child)
    return clone_root