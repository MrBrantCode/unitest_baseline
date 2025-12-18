"""
QUESTION:
Write a function `isBalancedParentheses` that takes a string `s` containing a series of parentheses as input and returns `true` if the parentheses are balanced, and `false` otherwise. A string of parentheses is considered balanced if every opening parenthesis has a corresponding closing parenthesis and they are properly nested. The string `s` may contain three types of parentheses: '(', ')', '[', ']', '{', '}'.
"""

def isBalancedParentheses(s: str) -> bool:
    stack = []
    opening = set(['(', '[', '{'])
    closing = set([')', ']', '}'])
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != mapping[char]:
                return False
    
    return not stack