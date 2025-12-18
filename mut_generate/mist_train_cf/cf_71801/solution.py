"""
QUESTION:
Given a balanced parentheses string `S`, compute the score of the string based on the following rules:
- `()` has score 1
- `AB` has score `A + B`, where A and B are balanced parentheses strings.
- `(A)` has score `2 * A`, where A is a balanced parentheses string.
- The score of a string `S` is multiplied by the number of occurrences of `()` in `S`.
 
The input string `S` contains only `(` and `)` and its length is between 2 and 50 (inclusive). Write a function `scoreOfParentheses(S)` to compute the score of `S` based on the above rules.
"""

def scoreOfParentheses(S):
    stack = [0] 
    count = S.count('()')        # Count the number of occurrences of '()'
    
    # Go through the string, computing the score as before...
    for i in S:
        if i == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2 * v, 1)
    
    # ...but then multiply the final score by the count.
    return stack.pop() * count