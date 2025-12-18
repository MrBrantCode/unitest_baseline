"""
QUESTION:
Given an array A[] which represents a Complete Binary Tree i.e, if index i is the parent, index 2*i + 1 is the left child and index 2*i + 2 is the right child.
The task is to find the minimum number of swaps required to convert it into a Binary Search Tree. 
Example 1:
Input:
A[] = { 5, 6, 7, 8, 9, 10, 11 }
Output: 3
Explanation: 
Binary tree of the given array:
Swap 1: Swap node 8 with node 5.
Swap 2: Swap node 9 with node 10.
Swap 3: Swap node 10 with node 7.
So, minimum 3 swaps are required.
Example 2:
Input: 
A[] = {1, 2, 3}
Output: 1
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minSwaps() which takes an array A[] and returns an integer as output.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{5}
"""

from typing import List

class pair:
    def __init__(self, val, index):
        self.val = val
        self.index = index

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

def min_swaps_to_bst(A: List[int]) -> int:
    n = len(A)
    inorder = []

    def _inorder_traversal(index):
        if index >= n:
            return
        _inorder_traversal(2 * index + 1)
        inorder.append(A[index])
        _inorder_traversal(2 * index + 2)

    _inorder_traversal(0)
    temp = [pair(inorder[i], i) for i in range(n)]
    temp.sort()
    visited = [-1] * n
    ans = 0

    for index in range(n):
        cycle_size = 0
        curr_index = index
        while visited[curr_index] == -1:
            cycle_size += 1
            visited[curr_index] = 1
            curr_index = temp[curr_index].index
        if cycle_size > 0:
            ans += cycle_size - 1

    return ans