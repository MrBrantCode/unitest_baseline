"""
QUESTION:
Given two strings 'str' and a wildcard pattern 'pattern' of length N and M respectively,  You have to print '1' if the wildcard pattern is matched with str else print '0' .
The wildcard pattern can include the characters ‘?’ and ‘*’
‘?’ – matches any single character
‘*’ – Matches any sequence of characters (including the empty sequence)
Note: The matching should cover the entire str (not partial str).
 
Example 1:
Input:
pattern = "ba*a?"
str = "baaabab"
Output: 1
Explanation: replace '*' with "aab" and 
'?' with 'b'. 
Example 2:
Input:
pattern = "a*ab"
str = "baaabab"
Output: 0
Explanation: Because of'a' at first position,
pattern and str can't be matched. 
Your Task:
You don't need to read input or print anything. Your task is to complete the function wildCard() which takes the two strings 'pattern' and 'str' as input parameters and returns the answer.
 
Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)
Constraints:
1 <= length of(str,pat) <= 200
"""

def wildcard_match(pattern: str, string: str) -> int:
    def unique(p: str) -> bool:
        for char in p:
            if char != '*':
                return False
        return True

    def solve(s: str, p: str, m: int, n: int, dp: list) -> bool:
        if m == 0 and n == 0:
            return True
        if n == 0:
            return False
        if m == 0 and unique(p[:n]):
            return True
        if m == 0:
            return False
        if dp[m][n] != -1:
            return dp[m][n]
        if s[m - 1] == p[n - 1] or p[n - 1] == '?':
            dp[m][n] = solve(s, p, m - 1, n - 1, dp)
            return dp[m][n]
        if p[n - 1] == '*':
            flag = False
            for i in range(m + 1):
                flag = flag or solve(s, p, m - i, n - 1, dp)
                if flag:
                    dp[m][n] = True
                    return dp[m][n]
            dp[m][n] = flag
            return dp[m][n]
        dp[m][n] = False
        return dp[m][n]

    m = len(string)
    n = len(pattern)
    dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    return 1 if solve(string, pattern, m, n, dp) else 0