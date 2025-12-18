"""
QUESTION:
Create a function `extract_substrings(text)` that takes a string as input and returns a list of substrings enclosed within parentheses in the order of their appearance. The function should handle nested parentheses, special typographic symbols, and escape sequences. If the input string contains unbalanced parentheses, the function should return "Unbalanced parentheses".
"""

def extract_substrings(text):
    stack = [[]]
    for character in text:
        if character == '\\':
            continue  # Ignore escape sequences
        
        if character == '(':
            stack.append([]) # Add new level for nested parentheses
        elif character == ')':
            if len(stack) == 1:
                return "Unbalanced parentheses"
            
            # We're closing a parenthesis, so pop the stack and get the string
            finished_substring = ''.join(stack.pop())
            # Add this substring to the parent level on the stack
            stack[-1].append(finished_substring)
        else:
            # Add the characters to the string in the current pair of parentheses
            stack[-1].append(character)
    
    # If the parentheses were all balanced, the stack should look like this: [[]]
    if len(stack) != 1 or stack[0]:
        return "Unbalanced parentheses"
    
    # Returning all the strings we've found
    return stack[0]