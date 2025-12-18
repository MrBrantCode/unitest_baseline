"""
QUESTION:
Create a function `complex_brackets` that takes a list of strings restricted to open and close brackets '{', '}', '[', ']', '(', ')' as input. The function should check if a correct merging order exists, creating a string with accurate nested brackets. Return 'True' if a possible arrangement exists, or 'False' if otherwise. The input list must contain a minimum of two strings.
"""

def complex_brackets(lst):
    brackets = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    input_string = ''.join(lst)
    stack = []
    for bracket in input_string:
        if bracket in brackets.values():   
            stack.append(bracket)
        elif bracket in brackets.keys():   
            if stack == [] or brackets[bracket] != stack.pop(): 
                return False
    return stack == []   