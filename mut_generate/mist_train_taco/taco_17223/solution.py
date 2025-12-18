"""
QUESTION:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
 
Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

 
Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""

def longest_valid_parentheses(s: str) -> int:
    memo = {}
    n = len(s)

    def dp(i):
        if i <= 0:
            return 0
        if i in memo:
            return memo[i]
        if (s[i - 1], s[i]) == ('(', ')'):
            memo[i] = dp(i - 2) + 2
        elif (s[i - 1], s[i]) == (')', ')') and i - dp(i - 1) - 1 >= 0 and (s[i - dp(i - 1) - 1] == '('):
            memo[i] = dp(i - 1) + 2 + dp(i - dp(i - 1) - 2)
        else:
            memo[i] = 0
        return memo[i]
    
    ret = 0
    for i in range(n - 1, 0, -1):
        ret = max(ret, dp(i))
    return ret