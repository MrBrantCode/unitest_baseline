"""
QUESTION:
Given two strings S and T, find length of the shortest subsequence in S which is not a subsequence in T. If no such subsequence is possible, return -1. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. A string of length n has  different possible subsequences.
 
Example 1:
Input:
S = "babab"
T = "babba"
Output:
3
Explanation:
There are no subsequences of S with
length less than 3 which is not a
subsequence of T. "aab" is an example of
a subsequence of length 3 which isn't a
subsequence of T.
Example 2:
Input:
S = "babhi"
T = "babij"
Output:
1
Explanation:
"h" is a subsequence of S that is
not a subsequence of T.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function shortestUnSub() which takes two Strings S, and T as input and returns the shortest Uncommon Subsequence.
 
Expected Time Complexity: O(|S|^{2}*|T|)
Expected Auxiliary Space: O(|S|*|T|)
 
Constraints:
1 <= |S|, |T| <= 500
"""

def shortest_uncommon_subsequence(S: str, T: str) -> int:
    m = len(S)
    n = len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the dp array
    for i in range(n + 1):
        dp[0][i] = 501
    for i in range(1, m + 1):
        dp[i][0] = 1
    
    # Fill the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            k = j - 1
            ch = S[i - 1]
            while k >= 0 and T[k] != ch:
                k -= 1
            if k == -1:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i - 1][k])
    
    # Get the result
    ans = dp[m][n]
    if ans >= 501:
        ans = -1
    
    return ans