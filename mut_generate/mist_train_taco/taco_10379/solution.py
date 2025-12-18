"""
QUESTION:
Given a string str consisting of digits, one may group these digits into sub-groups while maintaining their original order.
The task is to count number of groupings such that for every sub-group except the last one, sum of digits in a sub-group is less than or equal to sum of the digits in the sub-group immediately on its right.
For example, a valid grouping of digits of number 1119 is (1-11-9). Sum of digits in first subgroup is 1, next subgroup is 2, and last subgroup is 9. Sum of every subgroup is less than or equal to its immediate right.
 
Example 1: 
Input: str = "1119"
Output: 7
Explanation: [1-119], [1-1-19], [1-11-9], 
[1-1-1-9], [11-19], [111-9] and [1119] 
are seven sub-groups.
Example 2:
Input: str = "12"
Output: 2
Explanation: [1-2] and [12] are two sub-groups.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function TotalCount() which takes the string str as input parameter and returns total possible groupings.
Expected Time Complexity: O(N * N ) where N is length of string.
Expected Space Complexity: O(N * N)
 
Constraints:
1 <= length of string <= 100
"""

from functools import lru_cache

def count_valid_groupings(s: str) -> int:
    n = len(s)
    sums = [[0] * n for _ in range(n)]
    
    # Precompute the sums of all possible sub-groups
    for r in range(n - 1, -1, -1):
        for l in range(r, -1, -1):
            if l == r:
                sums[l][r] = int(s[l])
            else:
                sums[l][r] = int(s[l]) + sums[l + 1][r]

    @lru_cache(None)
    def count(n, start):
        if len(s[start:]) == 0:
            return 1
        cnt = 0
        for i in range(start + 1, len(s) + 1):
            nxt_n = sums[start][i - 1]
            if nxt_n >= n:
                cnt += count(nxt_n, i)
        return cnt
    
    return count(0, 0)