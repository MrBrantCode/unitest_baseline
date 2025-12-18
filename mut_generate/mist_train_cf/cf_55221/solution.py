"""
QUESTION:
Construct a function `verify_brackets` that takes an array of two strings composed only of '(' and ')' as input and determines whether these strings can be concatenated to form a valid sequence of nested brackets. The function should return 'Yes' if a valid string can be formed, and 'No' otherwise.
"""

def verify_brackets(arr): 
    stack = [] 
    for str in arr:
        for ch in str:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if not stack:
                    return 'No'
                stack.pop()
    return 'Yes' if not stack else 'No'