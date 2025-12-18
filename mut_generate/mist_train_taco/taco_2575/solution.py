"""
QUESTION:
Given string s containing characters as integers only, the task is to delete all characters of this string in a minimum number of steps wherein one step you can delete the substring which is a palindrome. After deleting a substring remaining parts are concatenated.
Example 1:
Input: s = "2553432"
Output: 2
Explanation: In first step remove "55", 
then string becomes "23432" which is a 
palindrome.
Example 2:
Input: s = "1234"
Output: 4
Explanation: Remove each character in 
each step
Your Task:  
You don't need to read input or print anything. Complete the function minStepToDeleteString() which string s as input parameters and returns the integer value
Expected Time Complexity: O(|s|^{3})
Expected Auxiliary Space: O(|s|^{2})
Constraints:
1 ≤ |s| ≤ 10^{3}
"""

def min_steps_to_delete_string(s: str) -> int:
    def solve(s, dp, start, end):
        if start > end:
            return 0
        if start == end:
            return 1
        if dp[start][end] != -1:
            return dp[start][end]
        
        op1 = op2 = op3 = float('inf')
        op1 = 1 + solve(s, dp, start + 1, end)
        
        if s[start] == s[start + 1]:
            op2 = 1 + solve(s, dp, start + 2, end)
        
        for i in range(start + 2, end + 1):
            if s[start] == s[i]:
                op3 = min(op3, solve(s, dp, start + 1, i - 1) + solve(s, dp, i + 1, end))
        
        dp[start][end] = min(op1, op2, op3)
        return dp[start][end]
    
    n = len(s)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return solve(s, dp, 0, n - 1)