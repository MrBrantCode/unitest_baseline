"""
QUESTION:
Given two strings X and Y, the task is to check if it is possible to convert X to Y by performing the following operations.
	 Make some lowercase letters uppercase.
	 Delete all the lowercase letters.
NOTE: You can perform one,two or none operations to convert the string X to Y as needed.
Example 1:
Input: X = "daBcd", Y = "ABC"
Output: 1
Explanation: Convert 'a' and 'c', delete
both the d's
Example 2:
Input: X = "ABcd", Y = "BCD"
Output: 0
Explanation: Can not delete A
Your Task:  
You don't need to read input or print anything. Your task is to complete the function stringConversion() which takes the strings as input and returns 1 if it is possible to convert, otherwise 0.
Expected Time Complexity: O(|X|*|Y|)
Expected Auxiliary Space: O(|X|*|Y|)
Constraints:
1 ≤ |X|, |Y| ≤ 10^{3}
"""

def can_convert_string(X: str, Y: str) -> int:
    n = len(X)
    m = len(Y)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] if X[i - 1].islower() else 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1].upper() == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            if X[i - 1].islower():
                dp[i][j] = dp[i][j] or dp[i - 1][j]
    
    return dp[n][m]