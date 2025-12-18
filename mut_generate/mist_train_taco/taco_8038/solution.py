"""
QUESTION:
You are given a tree rooted at node 1. The tree is given in form of an array P where P_{i} denotes the parent of node i, Also P_{1} = -1, as node 1 is the root node. Every node i has a value A_{i} associated with it. At first, you have to choose any node to start with, after that from a node you can go to any of its child nodes. You've to keep moving to a child node until you reach a leaf node. Every time you get to a new node, you write its value. Let us assume that the integer sequence in your path is B.
Let us define a function f over B, which is defined as follows:
f(B) = B_{1} - B_{2} + B_{3} - B_{4} + B_{5}.... + (-1)^{(k-1)}B_{k}.
You have to find the maximum possible value of f(B).
Example 1:
Input:
N = 3,
A = { 1, 2, 3}
P = {-1, 1, 1}
Output:
3
Explanation:
The resulting tree is:
        1(1)
      /     \
     2(2)   3(3)
If we choose our starting node as 3, then the
resulting sequence will be B = { 3 },
which will give the maximum possible value.
Example 2:
Input:
N = 3,
A = { 3, 1, 2}
P = {-1, 1, 2}
Output:
4
Explanation:
The resulting tree is:
  1(3)
  |
  2(1)
  |
  3(2)
If we choose our starting node as 1, then the
resulting sequence will be B = { 3 , 1 , 2 }.
The value which we'll get is, 3-1+2 = 4, which
is the maximum possible value.
Your Task:
The task is to complete the function bestNode() which takes an integer N and two integer arrays A, P as input parameters and returns the maximum possible value possible.
Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
Constraints:
1 ≤  N ≤ 10^{5}
-10^{5} ≤  A_{i} ≤ 10^{5}
-1 ≤  P_{i} ≤ N
"""

from typing import List

def best_node(N: int, A: List[int], P: List[int]) -> int:
    def _solve(ix):
        if cs[ix]:
            for c in cs[ix]:
                _solve(c)
            dp[ix] = max((A[ix] - A[i] + cmax[i] for i in cs[ix]))
            cmax[ix] = max((dp[i] for i in cs[ix]))
        else:
            dp[ix] = A[ix]
            cmax[ix] = 0
    
    cs = [[] for _ in range(N)]
    (dp, cmax) = ([0] * N, [0] * N)
    
    for i in range(1, N):
        cs[P[i] - 1].append(i)
    
    _solve(0)
    return max(dp)