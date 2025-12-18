"""
QUESTION:
Design a function named `remove_brackets` that removes parentheses and their contents from a given string, considering nested parentheses and handling multiple bracket types concurrently, including square and curly brackets, while ignoring any unmatched closing brackets. The function should be efficient for strings up to 10,000 characters in length.
"""

def remove_brackets(s):
    open_brackets = set(['(', '[', '{'])
    close_brackets = set([')', ']', '}'])
    match_brackets = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    remove = [False]*len(s)
    
    for i, char in enumerate(s):
        if char in open_brackets:
            stack.append((char, i))
        elif char in close_brackets:
            if stack and (stack[-1][0], char) in match_brackets:
                _, open_id = stack.pop()
                remove[open_id] = remove[i] = True
                
    return ''.join([s[i] for i in range(len(s)) if not remove[i]])