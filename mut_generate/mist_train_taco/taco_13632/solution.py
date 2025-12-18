"""
QUESTION:
Given an array of size N containing level order traversal of a BST. The task is to complete the function constructBst(), that construct the BST (Binary Search Tree) from its given level order traversal.
Example 1:
Input:
N = 9
BST[] = {7,4,12,3,6,8,1,5,10}
Output: 7 4 3 1 6 5 12 8 10
Explanation: After constructing BST, the
preorder traversal of BST is
7 4 3 1 6 5 12 8 10.
Example 2:
Input:
N = 6
BST[] = {1,3,4,6,7,8}
Output: 1 3 4 6 7 8
Explanation: After constructing BST, the
preorder traversal of BST is 1 3 4 6 7 8.
Your Task:
Your task is to complete the function constructBst() which has two arguments, first as the array containing level order traversal of BST and next argument as the length of array which return the root of the newly constructed BST. The preorder traversal of the tree is printed by the driver's code.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N).
Constraints:
1 <= N <= 10^{3}
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_bst_from_level_order(level_order_traversal):
    if not level_order_traversal:
        return None
    
    n = len(level_order_traversal)
    Q = []
    i = 1
    
    root = Node(level_order_traversal[0])
    Q.append([root, float('-inf'), float('inf')])
    
    while i < n and Q:
        temp = Q.pop(0)
        if i < n and level_order_traversal[i] < temp[0].data and (level_order_traversal[i] > temp[1]):
            temp[0].left = Node(level_order_traversal[i])
            Q.append([temp[0].left, temp[1], temp[0].data])
            i += 1
        if i < n and level_order_traversal[i] > temp[0].data and (level_order_traversal[i] < temp[2]):
            temp[0].right = Node(level_order_traversal[i])
            Q.append([temp[0].right, temp[0].data, temp[2]])
            i += 1
    
    return root