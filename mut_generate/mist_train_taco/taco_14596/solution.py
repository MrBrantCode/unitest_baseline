"""
QUESTION:
Write a function which outputs the positions of matching bracket pairs. The output should be a dictionary with keys the positions of the open brackets '(' and values the corresponding positions of the closing brackets ')'.

For example: input = "(first)and(second)" should return {0:6, 10:17}

If brackets cannot be paired or if the order is invalid (e.g. ')(') return False. In this kata we care only about the positions of round brackets '()', other types of brackets should be ignored.
"""

def find_matching_bracket_positions(string: str) -> dict or bool:
    brackets = {}
    open_brackets = []
    
    for i, c in enumerate(string):
        if c == '(':
            open_brackets.append(i)
        elif c == ')':
            if not open_brackets:
                return False
            brackets[open_brackets.pop()] = i
    
    return False if open_brackets else brackets