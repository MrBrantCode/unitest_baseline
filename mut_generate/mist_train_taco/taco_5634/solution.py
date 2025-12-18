"""
QUESTION:
Given a number N, find the total number of possible X such that (N XOR X) == (N OR X), where 0<=X<=N.
Example 1:
Input: N = 5
Output: 2
Explanation:
5 XOR 2 == 5 OR 2 and 
5 XOR 0 == 5 OR 0
Example 2:
Input: N = 7
Output: 1
Explanation: 7 XOR 0 == 7 OR 0
Your Task:
You don't need to read or print anything. Your task is to complete the function total_count() which takes N as input parameter and returns total count of X. 
 
Expected Time Complexity: O(log(N))
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{18}
"""

def count_valid_X(n: int) -> int:
    cnt = 0
    for i in range(64):
        if (1 << i) <= n and (1 << i) & n == 0:
            cnt += 1
    return 1 << cnt