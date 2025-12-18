"""
QUESTION:
Given an NxN chessboard and a Knight at position (x, y). The Knight has to take exactly K steps, where at each step it chooses any of the 8 directions uniformly at random. Find the probability that the Knight remains in the chessboard after taking K steps, with the condition that it cant enter the board again once it leaves it.
 
Example 1:
Input : N = 8, x = 0, y = 0, K = 3
Output: 0.125000
Example 2:
Input: N = 4, x = 1, y = 2, k = 4
Output: 0.024414
 
Your Task: 
You don't need to read or print anything. Your task is to complete the function findProb() which takes N, x, y and K as input parameter and returns the probability.
 
Expected Time Complexity : O(N ^{3})
Expected Space Complexity: O(N^{3})
 
Constraints:
1 <= N <= 100
0 <= x, y <= N
0 <= K <= N
"""

from functools import lru_cache

def find_knight_probability(N, x, y, K):
    dir = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

    @lru_cache(None)
    def solve(x, y, t):
        if not (0 <= x < N and 0 <= y < N):
            return 0
        if t == 0:
            return 1
        ans = 0
        for (i, j) in dir:
            ans += solve(x + i, y + j, t - 1)
        return ans
    
    return solve(x, y, K) / 8 ** K