"""
QUESTION:
Create a function named check_brackets that takes a string of brackets as input. The function should return True if the brackets are correctly matched and False otherwise. The input string contains only three types of brackets: square brackets ([]), curly brackets ({}), and parentheses (()). A pair of brackets is correctly matched if the opening bracket appears before the corresponding closing bracket, and there is no mismatch in the types of brackets. The function should handle cases with multiple pairs of brackets.
"""

def check_brackets(bracket_string):
    """
    Function that checks if bracket string is correctly matched.
    """
    stack = []
    open_brackets = {'[', '{', '('}
    close_brackets = {']': '[', '}': '{', ')': '('}
    
    for bracket in bracket_string:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackets:
            if not stack or close_brackets[bracket] != stack.pop():
                return False
        
    return not stack