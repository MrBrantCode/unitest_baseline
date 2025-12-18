"""
QUESTION:
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces  . The integer division should truncate toward zero.

Example 1:


Input: "3+2*2"
Output: 7


Example 2:


Input: " 3/2 "
Output: 1

Example 3:


Input: " 3+5 / 2 "
Output: 5


Note:


       You may assume that the given expression is always valid.
       Do not use the eval built-in library function.
"""

def evaluate_expression(expression: str) -> int:
    if not expression:
        return 0
    
    pre_op = '+'
    stack = [0]
    cur_num = 0
    digits = '0123456789'
    expression += '#'
    
    for c in expression:
        if c == ' ':
            continue
        if c in digits:
            cur_num = cur_num * 10 + int(c)
            continue
        if pre_op == '-':
            cur_num *= -1
        elif pre_op == '*':
            cur_num *= stack.pop()
        elif pre_op == '/':
            if cur_num == 0:
                return None
            pre_num = stack.pop()
            flag = 1 if pre_num > 0 else -1
            cur_num = abs(pre_num) // cur_num * flag
        stack.append(cur_num)
        pre_op = c
        cur_num = 0
    
    return sum(stack)