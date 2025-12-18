"""
QUESTION:
Given an infix expression in the form of string str. Convert this infix expression to postfix expression.
	Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
	Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
	Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. 
Example 1:
Input: str = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be abcd^e-fgh*+^*+i-
Example 2:
Input: str = "A*(B+C)/D"
Output: ABC+*D/
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be ABC+*D/
 
Your Task:
This is a function problem. You only need to complete the function infixToPostfix() that takes a string(Infix Expression) as a parameter and returns a string(postfix expression). The printing is done automatically by the driver code.
Expected Time Complexity: O(|str|).
Expected Auxiliary Space: O(|str|).
Constraints:
1 ≤ |str| ≤ 10^{5}
"""

def infix_to_postfix(infix_expression: str) -> str:
    def is_operand(ch: str) -> bool:
        return ch.isalpha() or ch.isdigit()

    output = ''
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for char in infix_expression:
        if is_operand(char):
            output += char
        elif not stack:
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        elif stack[-1] == '(' and (char == '+' or char == '-' or char == '*' or char == '/' or char == '^'):
            stack.append(char)
        elif char in precedence and (stack[-1] not in precedence or precedence[char] > precedence[stack[-1]]):
            stack.append(char)
        else:
            while stack and stack[-1] != '(' and (char not in precedence or precedence[char] <= precedence[stack[-1]]):
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    return output