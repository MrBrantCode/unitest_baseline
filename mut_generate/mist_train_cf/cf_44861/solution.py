"""
QUESTION:
Write a function named `count_brackets` that takes a string of brackets as input and returns three integers representing the counts of balanced parentheses, square brackets, and curly braces, respectively. The function should correctly handle nested brackets. The input string may contain any combination of '(', ')', '[', ']', '{', and '}' characters.
"""

def count_brackets(string):
    
    count_round = count_curly = count_square = 0
    
    stack = []
    
    for bracket in string:
        
        stack.append(bracket)
        
        if len(stack) < 2:
            
            continue
            
        if stack[-2] == '(' and stack[-1] == ')':
            
            count_round += 1
            stack = stack[:-2]
            
        elif stack[-2] == '[' and stack[-1] == ']':
            
            count_square += 1
            stack = stack[:-2]
            
        elif stack[-2] == '{' and stack[-1] == '}':
            
            count_curly += 1
            stack = stack[:-2]
            
    return count_round, count_square, count_curly