"""
QUESTION:
Given an integer N, the task is to find the number of ways we can choose 3 numbers from {1, 2, 3, …, N} such that their sum is even.
Note: Answer can be very large, output answer modulo 10^{9}+7
Example 1:
Input: N = 3
Output: 1
Explanation: Select {1, 2, 3}
Example 2:
Input: N = 4
Output: 2
Explanation: Either select {1, 2, 3} or 
{1, 3, 4}
Your Task:  
You don't need to read input or print anything. Complete the function countWays() which takes N as input parameter and returns the integer value.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
"""

def count_ways_to_choose_even_sum(N: int) -> int:
    mod = 10**9 + 7
    n = N // 2
    
    if N % 2 == 0:
        ans = n * (n - 1) * (n - 2) // 6 + n * (n - 1) // 2 * n
    else:
        ans = n * (n - 1) * (n - 2) // 6 + (n + 1) * n // 2 * n
    
    return ans % mod