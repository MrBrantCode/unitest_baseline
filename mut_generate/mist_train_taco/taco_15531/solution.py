"""
QUESTION:
Given two arrays that represent Preorder traversals of a Full binary tree preOrder[] and its mirror tree preOrderMirror[], your task is to complete the function constructBinaryTree(), that constructs the full binary tree using these two Preorder traversals.
Note: It is not possible to construct a general binary tree using these two traversal. But it is possible to create a full binary tree using the above traversals without any ambiguity.
Example 1:
Input :
preOrder[] = {0,1,2}
preOrderMirror[] = {0,2,1} 
Output :
                0
              /   \
             1     2
Explanation :
Tree in the output and it's mirror tree matches the preOrder and preOrderMirror.
Example 2:
Input :  
preOrder[] = {1,2,4,5,3,6,7}
preOrderMirror[] = {1,3,7,6,2,5,4}
Output :          
                 1
               /    \
              2      3
            /   \   /  \
           4     5 6    7
Explanation :
Tree in the output and it's mirror tree matches the preOrder and preOrderMirror.
Your Task:
You don't need to read, input, or print anything. Your task is to complete the function constructBTree, The function takes three arguments as input, first the array that represent Preorder traversals of a Full binary tree preOrder[], second the array that represents the preorder traversal of its mirror tree preOrderMirror[] and last the size of both the array,and returns root of the full binary tree.
Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(N), where N indicates number of nodes.
Constraints:
1 <= Number of Nodes <= 10^{3}
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def construct_full_binary_tree(preorder, preorder_mirror, n):
    def util(pre, preM, n):
        if i[0] == n:
            return None
        j = 0
        while j < n:
            if preM[j] == pre[i[0]]:
                break
            j += 1
        preM[j] = -1
        root = Node(pre[i[0]])
        i[0] += 1
        if j == n - 1 or preM[j + 1] == -1:
            return root
        root.left = util(pre, preM, n)
        root.right = util(pre, preM, n)
        return root
    
    i = [0]  # Using a list to simulate a mutable integer for the index
    return util(preorder, preorder_mirror, n)