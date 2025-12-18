"""
QUESTION:
Write a function `remove_comments(code)` that takes a string of multiple lines of code as input and returns the modified code with all comments removed. Comments start with the string '#'. The function should handle single-line and multi-line comments correctly, where multi-line comments start with '#' and end with '#'. The solution must have a time complexity of O(n), where n is the total number of characters in the input string, and cannot use any external libraries or built-in functions to remove the comments.
"""

def remove_comments(code):
    lines = code.split('\n')
    in_comment = False
    new_code = []
    for line in lines:
        i = 0
        while i < len(line):
            if line[i] == '#':
                if not in_comment:
                    line = line[:i]
                    break
                else:
                    i += 1
            elif line[i:i+2] == '##':
                if not in_comment:
                    in_comment = True
                    line = line[:i]
                else:
                    i += 2
            elif line[i:i+2] == '##':
                if in_comment:
                    in_comment = False
                    line = line[i+2:]
                else:
                    i += 2
            else:
                i += 1
        new_code.append(line)
    return '\n'.join(new_code)