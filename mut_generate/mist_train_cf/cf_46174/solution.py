"""
QUESTION:
Create a function `intricate_brackets` that evaluates the nesting order of multiple types of brackets in a given list of strings. The function should return 'Yes' if the brackets are properly nested and 'No' otherwise. The function should support the following types of brackets: '()', '{}', '[]', and '<>'. The input list may contain single characters or strings with multiple characters.
"""

def intricate_brackets(lst):
    opening_brackets = ['(','{','[','<']
    closing_brackets = [')','}',']','>']
    brackets_dict = {')':'(','}':'{',']':'[','>':'<'}
    stack = []
    for bracket in lst:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or brackets_dict[bracket] != stack.pop():
                return 'No'
    if stack:
        return 'No'
    return 'Yes'