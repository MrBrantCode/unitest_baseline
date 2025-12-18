"""
QUESTION:
Given a string, the task is to count all palindromic sub-strings present in it. Length of palindrome sub-string must be greater than or equal to 2. 
Example
Input
N = 5
str = "abaab"
Output
3
Explanation:
All palindrome substring are : "aba" , "aa" , "baab"
Example
Input
N = 7
str = "abbaeae"
Output
4
Explanation:
All palindrome substring are : "bb" , "abba" ,"aea",
"eae"
Expected Time Complexity : O(|S|^{2})
Expected Auxilliary Space : O(|S|^{2})
Constraints:
2<=|S|<=500
"""

def count_palindromic_substrings(s: str, n: int) -> int:
    count = 0
    dp = [[False] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1
    
    # Check for substrings of length greater than 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1
    
    return count