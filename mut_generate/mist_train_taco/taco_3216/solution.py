"""
QUESTION:
Given a postfix expression. Your task is to complete the method constructTree(). The output of the program will print the infix expression of the given postfix expression.
Input:
The constructTree() function takes a single argument as input, character array containing the given postfix expression.
Output:
Infix expression should be printed for each given postfix expression.
Constraints:
1<=T<=50
1<=length_of_expression<=40
Example:
Input:
2
ab+ef*g*-
wlrb+-*
Output:
a + b - e * f * g
w * l - r + b
Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.
"""

def postfix_to_infix(postfix: str) -> str:
    def is_operator(i: str) -> bool:
        return i in ['*', '^', '/', '+', '-']

    class et:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    stack = []
    for i in postfix:
        if not is_operator(i):
            q = et(i)
            stack.append(q)
        else:
            right_child = stack.pop()
            left_child = stack.pop()
            q = et(f"({left_child.value} {i} {right_child.value})")
            stack.append(q)
    
    return stack.pop().value