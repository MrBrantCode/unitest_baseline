"""
QUESTION:
Reverse Polish Notation (RPN) is a mathematical notation where every operator follows all of its operands. For instance, to add three and four, one would write "3 4 +" rather than "3 + 4". If there are multiple operations, the operator is given immediately after its second operand; so the expression written "3 − 4 + 5" would be written "3 4 − 5 +" first subtract 4 from 3, then add 5 to that.

Transform the algebraic expression with brackets into RPN form. 

You can assume that for the test cases below only single letters will be used, brackets [] will not be used and each expression has only one RPN form (no expressions like a*b*c)

----- Sample Input 1 ------ 
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

----- Sample Output 1 ------ 
abc*+
ab+zx+*
at+bac++cd+^*
"""

def infix_to_rpn(expression: str) -> str:
    stack = []
    result = ''
    
    for char in expression:
        if ord(char) in range(97, 123):  # Check if the character is a lowercase letter
            result += char
        elif char == ')':
            if stack:
                result += stack.pop()
        elif char == '(':
            continue
        else:
            stack.append(char)
    
    return result