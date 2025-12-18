"""
QUESTION:
Given a string `S` consisting of `(` and `)` characters, write a function `minAddToMakeValid` that returns the minimum number of parentheses that must be added to make the resulting string both valid and a palindrome. The function should take a string `S` as input, where `S.length <= 1000`.
"""

def minAddToMakeValid(S: str) -> int:
    def minAdd(S: str) -> int:
        stack = []
        for char in S:
            if char == '(':
                stack.append('(')
            elif not stack:
                stack.append(')')
            elif ((char == ')' and stack[-1] == '(') or
                  (char == '(' and stack[-1] == ')')):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
    return max(minAdd(S), minAdd(S[::-1]))