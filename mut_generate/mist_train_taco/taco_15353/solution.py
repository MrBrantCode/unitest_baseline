"""
QUESTION:
A frog jumps either 1, 2, or 3 steps to go to the top. In how many ways can it reach the top. As the answer will be large find the answer modulo 1000000007.
Example 1:
Input:
N = 1
Output: 1
Example 2:
Input:
N = 4
Output: 7
Explanation:Below are the 7 ways to reach
4
1 step + 1 step + 1 step + 1 step
1 step + 2 step + 1 step
2 step + 1 step + 1 step
1 step + 1 step + 2 step
2 step + 2 step
3 step + 1 step
1 step + 3 step
Your Task:
Your task is to complete the function countWays() which takes 1 argument(N) and returns the answer%(10^9 + 7).
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{5}
"""

def count_ways_to_top(n: int) -> int:
    MOD = 1000000007
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    s1, s2, s3 = 1, 2, 4
    
    for i in range(4, n + 1):
        ways = (s1 + s2 + s3) % MOD
        s1, s2, s3 = s2, s3, ways
    
    return ways