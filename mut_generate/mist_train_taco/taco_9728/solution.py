"""
QUESTION:
You are given an array nodes. It contains 7 integers, which represents the value of nodes of the binary tree in level order traversal. You are also given a root of the tree which has a value equal to nodes[0].
Your task to construct a binary tree by creating nodes for the remaining 6 nodes.
Example:
Input: 
nodes = [1 2 3 4 5 6 7]
Output: 
         1
       /   \
     2       3
   /  \     /  \
   4  5    6   7
Explanation: 
The 7 node binary tree is represented above.
Your Task:
Complete the function void create_tree(node* root0, vector &vec), which takes a root of a Binary tree and vector array vec containing the values of nodes.
Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).
Constraints:
vec.length = 7
1<=vec[i]<=100
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_binary_tree(nodes):
    if len(nodes) != 7:
        raise ValueError("The input list must contain exactly 7 elements.")
    
    root = Node(nodes[0])
    root.left = Node(nodes[1])
    root.right = Node(nodes[2])
    root.left.left = Node(nodes[3])
    root.left.right = Node(nodes[4])
    root.right.left = Node(nodes[5])
    root.right.right = Node(nodes[6])
    
    return root