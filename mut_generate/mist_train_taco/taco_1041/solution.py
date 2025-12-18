"""
QUESTION:
Given a Binary tree and a key in the binary tree, find the node right to the given key. If there is no node on right side, then return a node with value -1.
Example 1:
Input:
       10
     /    \
    2      6
   / \      \
  8   4      5
and key = 2
Output: 6
Explanation: We can see in the above tree
that the next right node of 2 is 6.
Example 2:
Input:
      10
    /     \
   2       6
  / \       \
 8   4       5
and key = 5
Output: -1
Explanation: We can see in the above tree 
that there's No next right node of 5.
So, the output is -1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function nextRight() which takes root node of the tree and an integer key as input parameters and returns the next right node of the node with value key. 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1<=N<=10^{3}
1<=data of node<=10^{3}
1<=key<=10^{3}
"""

from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def find_next_right_node(root, key):
    if not root:
        return Node(-1)
    
    q = deque()
    q.append(root)
    
    while q:
        level_size = len(q)
        for i in range(level_size):
            current_node = q.popleft()
            
            if current_node.data == key:
                if i < level_size - 1:
                    return q.popleft()
                else:
                    return Node(-1)
            
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
    
    return Node(-1)