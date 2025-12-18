"""
QUESTION:
Given a string 'str' of size ‘n’. The task is to remove or delete the minimum number of characters from the string so that the resultant string is a palindrome. Find the minimum numbers of characters we need to remove.
Note: The order of characters should be maintained.
Example 1:
Input: n = 7, str = "aebcbda"
Output: 2
Explanation: We'll remove 'e' and
'd' and the string become "abcba".
Ã¢â¬â¹Example 2:
Input: n = 3, str = "aba"
Output: 0
Explanation: We don't remove any
character.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minDeletions() which takes the string s and length of s as inputs and returns the answer.
Expected Time Complexity: O(|str|^{2})
Expected Auxiliary Space: O(|str|^{2})
Constraints:
1 ≤ |str| ≤ 10^{3}
"""

def min_deletions_to_palindrome(str, n):
    s1 = str
    s2 = str[::-1]
    t = [[-1 for i in range(n + 1)] for i in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    
    x = t[n][n]
    return n - x