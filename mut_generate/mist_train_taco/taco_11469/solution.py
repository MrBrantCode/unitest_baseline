"""
QUESTION:
There are N points on the road ,you can step ahead by 1 or 2 . Find the number of ways you can reach at point N. 
Example 1:
Input: N = 4
Output: 5
Explanation: Three ways to reach at 4th
point. They are {1, 1, 1, 1}, {1, 1, 2},
{1, 2, 1} {2, 1, 1}, {2, 2}.
Example 2:
Input: N = 5
Output: 8
Explanation: Three ways to reach at 5th
point. They are {1, 1, 1, 1, 1},
{1, 1, 1, 2}, {1, 1, 2, 1}, {1, 2, 1, 1},
{2, 1, 1, 1}{1, 2, 2}, {2, 1, 2}, {2, 2, 1}
Your Task:
You don't need to read or print anyhting. Your task is to complete the function nthPoint() which takes N as input parameter and returns the total number of ways modulo 10^{9} + 7 to reach at Nth point.
Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
Constraints:
1 ≤ N ≤ 10^{4}
"""

def count_ways_to_reach_point(n: int) -> int:
    mod = 10**9 + 7
    
    if n <= 0:
        return 0
    if n <= 1:
        return 1
    if n <= 2:
        return 2
    
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
    
    for i in range(3, n + 1):
        ways[i] = (ways[i - 1] % mod + ways[i - 2] % mod) % mod
    
    return ways[n]