"""
QUESTION:
Write a function named `extract_substrings` that takes a string `text` as input. The function should extract all substrings encapsulated within parentheses in the order of their appearance, handling nested parentheses and unique typographic symbols. It should also handle edge cases by returning an error message for unbalanced parentheses, null strings, and strings without parentheses.
"""

def extract_substrings(text):
    if (not text) or (text == " "):
        return "Empty or null string"

    if text.count("(") != text.count(")"):
        return "Unbalanced brackets"

    stack = []
    result = []
    flag = False

    for i, c in enumerate(text):
        if c == '(':
            stack.append(i)
            flag = False
        elif c == ')':
            if stack:
                start = stack.pop()
                result.append(text[start+1:i])
                flag = False
            else:
                return "Unbalanced brackets"
        elif flag == False and not stack:
            flag = True
            
    if stack:
        return "Unbalanced brackets"

    if flag:
        return "String has no brackets"

    return result