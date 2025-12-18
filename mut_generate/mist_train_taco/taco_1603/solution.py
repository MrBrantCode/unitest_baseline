"""
QUESTION:
Given an integer S represented as a string, the task is to get the sum of all possible sub-strings of this string.
As the answer will be large, print it modulo 10^9+7.
Example 1:
Input:
S = 1234
Output: 1670
Explanation: Sum = 1 + 2 + 3 + 4 + 12 +
23 + 34 + 123 + 234 + 1234 = 1670
Example 2:
Input:
S = 421
Output: 491
Explanation: Sum = 4 + 2 + 1 + 42 + 21
Your Task:
You only need to complete the function sumSubstrings that takes S as an argument and returns the answer modulo 1000000007.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= |S| <= 10^{4}
"""

def sum_substrings(s: str) -> int:
    n = len(s)
    digits = [int(char) for char in s]
    dp = [0] * n
    dp[0] = digits[0]
    res = dp[0]
    
    for i in range(1, n):
        dp[i] = ((i + 1) * digits[i] + dp[i - 1] * 10) % 1000000007
        res += dp[i]
        res %= 1000000007
    
    return res