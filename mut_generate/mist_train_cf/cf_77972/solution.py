"""
QUESTION:
Create a function `match_brackets(lst)` that takes a list of strings, where each string contains only open or closed parentheses '(', ')', open or closed square brackets '[', ']', and open or closed curly brackets '{', '}'. The function should return 'Yes' if it's possible to order the strings to form a correctly nested and matching bracket layout, and 'No' otherwise.
"""

def match_brackets(lst):
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    open_brackets = set(['(', '[', '{'])
    stack = []
    for br in lst:
        for char in br:
            if char in open_brackets:  
                stack.append(char)
            elif stack and char == bracket_map[stack[-1]]:  
                stack.pop()
            else:  
                return 'No'
    return 'Yes' if not stack else 'No'