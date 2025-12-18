"""
QUESTION:
Write a function `count_character_in_parentheses` that takes two parameters: an `input_string` and a `character`. The function should count the number of times the `character` appears in the `input_string` only when it is surrounded by a pair of parentheses.
"""

def count_character_in_parentheses(input_string, character):
    count = 0
    inside_parentheses = False
    
    for char in input_string:
        if char == '(':
            inside_parentheses = True
        elif char == ')':
            inside_parentheses = False
        elif char == character and inside_parentheses:
            count += 1
    
    return count