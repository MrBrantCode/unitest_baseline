"""
QUESTION:
Create a function named `remove_brackets` that takes a string `s` as input. The function should remove all text enclosed within parentheses, square brackets, and curly brackets, handling nested brackets and disregarding unpaired closing brackets. The function should maintain the order of the remaining text and be efficient enough to handle strings with up to 10,000 characters.
"""

def remove_brackets(s: str) -> str:
    stack = []
    result = ''
    bracket_types = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        # If it's an opening bracket, push it onto the stack.
        if ch in set(bracket_types.values()):
            stack.append(ch)
        # If it's a closing bracket and the corresponding opening bracket is at the top of the stack, pop it.
        elif ch in bracket_types and stack and stack[-1] == bracket_types[ch]:
            stack.pop()
        # If it's not a bracket or it's an unpaired closing bracket, add it to the result if the stack is empty.
        elif not stack:
            result += ch
    return result