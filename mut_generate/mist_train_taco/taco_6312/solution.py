"""
QUESTION:
Given two strings s and t. Return the minimum number of operations required to convert s to t.
The possible operations are permitted:
	Insert a character at any position of the string.
	Remove any character from the string.
	Replace any character from the string with any other character.
 
Example 1:
Input: 
s = "geek", t = "gesek"
Output: 1
Explanation: One operation is required 
inserting 's' between two 'e's of s.
Example 2:
Input : 
s = "gfg", t = "gfg"
Output: 
0
Explanation: Both strings are same.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function editDistance() which takes strings s and t as input parameters and returns the minimum number of operation to convert the string s to string t. 
Expected Time Complexity: O(|s|*|t|)
Expected Space Complexity: O(|s|*|t|)
Constraints:
1 ≤ Length of both strings ≤ 100
Both the strings are in lowercase.
"""

def edit_distance(s: str, t: str) -> int:
    n = len(s)
    m = len(t)
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            dp[i][0] = i
            dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][m]