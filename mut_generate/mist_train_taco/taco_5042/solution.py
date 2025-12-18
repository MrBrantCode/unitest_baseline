"""
QUESTION:
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .

Example 1:


Input: "1 + 1"
Output: 2


Example 2:


Input: " 2-1 + 2 "
Output: 3

Example 3:


Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:


       You may assume that the given expression is always valid.
       Do not use the eval built-in library function.
"""

def evaluate_expression(expression: str) -> int:
    res = 0
    num = 0
    sign = 1
    stk = []
    
    for c in expression:
        if c.isdigit():
            num = 10 * num + (ord(c) - ord('0'))
        elif c == '+':
            res += sign * num
            num = 0
            sign = 1
        elif c == '-':
            res += sign * num
            num = 0
            sign = -1
        elif c == '(':
            stk.append(res)
            stk.append(sign)
            res = 0
            sign = 1
        elif c == ')':
            res += sign * num
            res *= stk.pop()
            res += stk.pop()
            num = 0
            sign = 1
    
    if num:
        res += sign * num
    
    return res