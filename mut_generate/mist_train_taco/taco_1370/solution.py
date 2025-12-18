"""
QUESTION:
Serialization is to store a tree in an array so that it can be later restored and Deserialization is reading tree back from the array. Now your task is to complete the function serialize which stores the tree into an array A[ ] and deSerialize which deserializes the array to the tree and returns it.
Note: The structure of the tree must be maintained. Multiple nodes can have the same data.
Example 1:
Input:
      1
    /   \
   2     3
Output: 2 1 3
Example 2:
Input:
         10
       /    \
      20    30
    /   \
   40  60
Output: 40 20 60 10 30
Your Task:
The task is to complete two functions serialize which takes the root node of the tree as input and stores the tree into an array and deSerialize which deserializes the array to the original tree and returns the root of it.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= Number of nodes <= 1000
1 <= Data of a node <= 1000
"""

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_serialization(root):
    if root is None:
        return []
    
    ans = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node is None:
            ans.append(None)
        else:
            ans.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
    
    while ans and ans[-1] is None:
        ans.pop()
    
    return ans

def tree_deserialization(serialized_list):
    if not serialized_list:
        return None
    
    root = Node(serialized_list[0])
    queue = deque([root])
    index = 1
    
    while queue and index < len(serialized_list):
        node = queue.popleft()
        
        if serialized_list[index] is not None:
            node.left = Node(serialized_list[index])
            queue.append(node.left)
        
        index += 1
        
        if index < len(serialized_list) and serialized_list[index] is not None:
            node.right = Node(serialized_list[index])
            queue.append(node.right)
        
        index += 1
    
    return root