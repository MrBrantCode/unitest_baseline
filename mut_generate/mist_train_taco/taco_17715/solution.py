"""
QUESTION:
You are installing a billboard and want it to have the largest height.  The billboard will have two steel supports, one on each side.  Each steel support must be an equal height.
You have a collection of rods which can be welded together.  For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.
Return the largest possible height of your billboard installation.  If you cannot support the billboard, return 0.
 
Example 1:
Input: [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.


Example 2:
Input: [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.



Example 3:
Input: [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.


 
Note:

0 <= rods.length <= 20
1 <= rods[i] <= 1000
The sum of rods is at most 5000.
"""

from functools import lru_cache
from typing import List

def tallest_billboard(rods: List[int]) -> int:
    rods = sorted(rods)[::-1]
    n = len(rods)
    psum = rods.copy()
    for i in range(n - 1)[::-1]:
        psum[i] += psum[i + 1]

    @lru_cache(None)
    def dfs(idx, diff):
        if idx == n:
            return 0 if diff == 0 else -float('inf')
        if diff > psum[idx]:
            return -float('inf')
        return max(dfs(idx + 1, diff), dfs(idx + 1, diff + rods[idx]), dfs(idx + 1, abs(diff - rods[idx])) + min(diff, rods[idx]))
    
    return dfs(0, 0)