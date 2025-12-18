"""
QUESTION:
Write a function `longestValidParentheses(s)` that takes a string `s` consisting of only '(' and ')' as input, where the length of `s` is between 0 and 3 * 10^4, inclusive. The function should return the length of the longest substring that forms a valid set of parentheses.
"""

def longestValidParentheses(s):
    max_len = 0
    stack = [-1] 

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i) 
        else:
            stack.pop() 
            if len(stack) != 0:
                max_len = max(max_len, i - stack[-1]) 
            else:
                stack.append(i)

    return max_len