"""
QUESTION:
Implement a function `calculate` that takes a string `s` representing a mathematical expression as input, parses the expression to create a stack data structure, and evaluates the resultant expression. The expression may contain the operators "+", "-", "*", "/", and parentheses to denote order of operations. The function should handle operator precedence and parenthetical expressions, and return the result of the expression as an integer. The input string does not contain whitespace characters.
"""

def calculate(s: str) -> int:
    num, stack, sign, res = 0, [], '+', 0
    
    for i in range(len(s)):
        if s[i].isdigit():
            num = num*10 + int(s[i])
        if s[i] in "+-*/(" or i == len(s)-1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            num = 0
            sign = s[i]
        if s[i] == ')' or i == len(s)-1:
            res += sum(stack)
            stack = []
                
    return res