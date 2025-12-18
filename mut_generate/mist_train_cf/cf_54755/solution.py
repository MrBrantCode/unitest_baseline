"""
QUESTION:
Write a function `check_math_notation(notation)` that checks if a given mathematical notation string is valid. The string can contain digits, common arithmetic operators (+, -, *, /, ^), and parentheses. The function should verify that the parentheses are well-balanced and the mathematical operations are in the correct order (i.e., no two operations are next to each other). The function should return "Correct" if the notation is valid, "Unbalanced" if the parentheses are not balanced, and "Incorrect Order" if the operations are not in the correct order. Assume that the input string does not contain any whitespace characters or other non-allowed characters.
"""

def check_math_notation(notation):
    open_list = ['('] 
    close_list = [')'] 

    stack_list = [] 

    #Check Parentheses Balance
    for i in notation: 
        if i in open_list: 
            stack_list.append(i) 
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack_list) > 0) and
                (open_list[pos] == stack_list[len(stack_list)-1])): 
                stack_list.pop()
            else: 
                return "Unbalanced"
    if len(stack_list) == 0: 
        #Checking operations' order
        prevChar = ''
        for char in notation:
            if prevChar in '+-*/^' and char in '+-*/^':
                return "Incorrect Order"
            if char != '(' and char != ')':
                prevChar = char 
        return "Correct"
    else: 
        return "Unbalanced"