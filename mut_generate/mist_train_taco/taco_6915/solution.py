"""
QUESTION:
Given two strings wild and pattern where wild string may contain wild card characters and pattern string is a normal string. Determine if the two strings match. The following are the allowed wild card characters in first string :-
* --> This character in string wild can be replaced by any sequence of characters, it can also be replaced by an empty string.
? --> This character in string wild can be replaced by any one character.
Example 1:
Input: wild = ge*ks
       pattern = geeks
Output: Yes
Explanation: Replace the '*' in wild string 
with 'e' to obtain pattern "geeks".
Example 2:
Input: wild = ge?ks*
       pattern = geeksforgeeks
Output: Yes
Explanation: Replace '?' and '*' in wild string with
'e' and 'forgeeks' respectively to obtain pattern 
"geeksforgeeks"
Your Task:
You don't need to read input or print anything. Your task is to complete the function match() which takes the string wild and pattern as input parameters and returns true if the string wild can be made equal to the string pattern, otherwise, returns false.
Expected Time Complexity: O(length of wild string * length of pattern string)
Expected Auxiliary Space: O(length of wild string * length of pattern string)
Constraints:
1<=length of the two string<=10^3
"""

def is_match(wild: str, pattern: str) -> bool:
    m = len(pattern)
    n = len(wild)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    dp[0][0] = True
    
    for j in range(1, n + 1):
        if wild[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == wild[j - 1] or wild[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif wild[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    
    return dp[m][n]