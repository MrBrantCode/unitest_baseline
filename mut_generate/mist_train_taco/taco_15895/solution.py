"""
QUESTION:
Given two strings S and T of length n and m respectively. Find count of distinct occurrences of T in S as a sub-sequence. 
 
Example 1:
Input:
S = "banana" , T = "ban"
Output: 3
Explanation: There are 3 sub-sequences:
[ban], [ba n], [b an].
Example 2:
Input:
S = "geeksforgeeks" , T = "ge"
Output: 6
Explanation: There are 6 sub-sequences:
[ge], [ ge], [g e], [g e] [g e] and [ g e].
Your Task:
You don't need to read input or print anything.Your task is to complete the function subsequenceCount() which takes two strings as argument S and T and returns the count of the sub-sequences modulo 10^{9} + 7.
Expected Time Complexity: O(n*m).
Expected Auxiliary Space: O(n*m).
Constraints:
1 ≤ length of(T) ≤ 100
1 ≤ length of(S) ≤ 8000
"""

def subsequence_count(S: str, T: str) -> int:
    n = len(S)
    m = len(T)
    
    if n < m:
        return 0
    
    # Initialize a 2D DP array with dimensions (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base case: There's one way to form an empty subsequence from any prefix of S
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            p1 = dp[i - 1][j]  # Number of ways to form T[0:j] using S[0:i-1]
            p2 = 0
            if S[i - 1] == T[j - 1]:
                p2 = dp[i - 1][j - 1]  # Number of ways to form T[0:j-1] using S[0:i-1]
            dp[i][j] = (p1 + p2) % 1000000007
    
    return dp[n][m]