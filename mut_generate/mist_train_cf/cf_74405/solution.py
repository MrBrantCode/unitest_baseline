"""
QUESTION:
Write a function `match_parens_and_brackets(lst)` that takes a list of two strings containing only opening and closing parentheses and brackets. The function should determine whether these strings can be arranged to form a correctly nested parentheses-brackets string and return 'Yes' if possible, 'No' otherwise. The function should handle nested parentheses and brackets.
"""

def match_parens_and_brackets(lst):
    # create mapping of matched parentheses
    brackets = {')': '(', ']': '['}
    # join strings for easy processing
    s = ''.join(lst)
    # stack used to handle brackets
    stack = []
    
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack == [] or brackets[char] != stack.pop():
                return "No"
    # if the stack is empty, all brackets were matched correctly
    return "Yes" if stack == [] else "No"