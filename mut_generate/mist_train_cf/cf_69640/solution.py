"""
QUESTION:
Given a list of strings `source` where each string represents a line of source code, write a function `removeComments(source)` that removes all comments from the source code and returns the resulting source code in the same format. 

The function should handle both line comments (denoted by `//`) and block comments (denoted by `/*` and `*/`). 

- A line comment causes all characters to its right on the same line to be disregarded.
- A block comment causes all characters until the next occurrence of `*/` to be disregarded, regardless of whether they are on the same line or not.
- If a line is empty after removing comments, it should not be included in the result.

The function should assume that every open block comment will eventually be closed, and that there are no single-quote, double-quote, or control characters in the source code. The length of `source` is between 1 and 100, and the length of each string in `source` is between 0 and 80.
"""

def removeComments(source):
    in_block = False
    ans = []
    for line in source:
        i = 0
        if not in_block:
            newline = []
        while i < len(line):
            if line[i:i+2] == '/*' and not in_block:
                in_block = True
                i += 1
            elif line[i:i+2] == '*/' and in_block:
                in_block = False
                i += 1
            elif not in_block and line[i:i+2] == '//':
                break
            elif not in_block:
                newline.append(line[i])
            i += 1
        if newline and not in_block:
            ans.append("".join(newline))
    return ans