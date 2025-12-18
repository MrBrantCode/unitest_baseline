"""
QUESTION:
Given a binary tree and a node data called target. Find the minimum time required to burn the complete binary tree if the target is set on fire. It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.
Note: The tree contains unique values.
Example 1:
Input:      
          1
        /   \
      2      3
    /  \      \
   4    5      6
       / \      \
      7   8      9
                   \
                   10
Target Node = 8
Output: 7
Explanation: If leaf with the value 
8 is set on fire. 
After 1 sec: 5 is set on fire.
After 2 sec: 2, 7 are set to fire.
After 3 sec: 4, 1 are set to fire.
After 4 sec: 3 is set to fire.
After 5 sec: 6 is set to fire.
After 6 sec: 9 is set to fire.
After 7 sec: 10 is set to fire.
It takes 7s to burn the complete tree.
Example 2:
Input:      
          1
        /   \
      2      3
    /  \      \
   4    5      7
  /    / 
 8    10
Target Node = 10
Output: 5
Your Task:  
You don't need to read input or print anything. Complete the function minTime() which takes the root of the tree and target as input parameters and returns the minimum time required to burn the complete binary tree if the target is set on fire at the 0th second.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(height of tree)
Constraints:
1 ≤ N ≤ 10^{4}
"""

from collections import deque, defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def min_time_to_burn_tree(root: Node, target: int) -> int:
    if not root:
        return 0
    
    que = deque()
    parentmap = defaultdict(Node)
    que.append(root)
    start = None
    
    # BFS to find the target node and build the parent map
    while que:
        curr = que.popleft()
        if curr.data == target:
            start = curr
        if curr.left:
            que.append(curr.left)
            parentmap[curr.left] = curr
        if curr.right:
            que.append(curr.right)
            parentmap[curr.right] = curr
    
    if not start:
        return 0  # Target node not found
    
    visited = set()
    visited.add(start)
    que.append(start)
    time = 0
    
    # BFS to burn the tree
    while que:
        size = len(que)
        for _ in range(size):
            curr = que.popleft()
            if curr.left and curr.left not in visited:
                que.append(curr.left)
                visited.add(curr.left)
            if curr.right and curr.right not in visited:
                que.append(curr.right)
                visited.add(curr.right)
            if curr in parentmap and parentmap[curr] not in visited:
                que.append(parentmap[curr])
                visited.add(parentmap[curr])
        time += 1
    
    return time - 1