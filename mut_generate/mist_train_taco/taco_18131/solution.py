"""
QUESTION:
Given a valid expression containing only binary operators '+', '-', '*', '/' and operands, remove all the redundant parenthesis.
A set of parenthesis is said to be redundant if, removing them, does not change the value of the expression.
Note: The operators '+' and '-' have the same priority. '*' and '/' also have the same priority. '*' and '/' have more priority than '+' and '-'.
Example 1:
Input:
Exp = (A*(B+C))
Output: A*(B+C)
Explanation: The outermost parenthesis
are redundant.
Example 2:
Input:
Exp = A+(B+(C))
Output: A+B+C
Explanation: All the parenthesis
are redundant.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function removeBrackets() which takes the string Exp as input parameters and returns the updated expression.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 < Length of Exp < 10^{5}
Exp contains uppercase english letters, '(' , ')', '+', '-', '*' and '/'.
"""

def remove_redundant_brackets(expression: str) -> str:
    stack = []
    priority = []
    ops = []
    
    for c in expression:
        if c == '(':
            ops.append(c)
        elif c == ')':
            op2 = stack.pop()
            pri = priority.pop()
            op = ops.pop()
            while op != '(':
                if op == '+' or op == '-':
                    pri = min(pri, 1)
                elif op == '*' or op == '/':
                    pri = min(pri, 2)
                op1 = stack.pop()
                pri = min(pri, priority.pop())
                op2 = op1 + op + op2
                op = ops.pop()
            if len(ops) > 0 and pri != 3:
                if ops[-1] == '/' or ((ops[-1] == '*' or ops[-1] == '-') and pri == 1):
                    op2 = '(' + op2 + ')'
            stack.append(op2)
            if op2[0] == '(':
                priority.append(3)
            else:
                priority.append(pri)
        elif c == '+' or c == '-':
            ops.append(c)
        elif c == '*':
            if priority[-1] == 1:
                op2 = stack.pop()
                if op2[0] != '(':
                    op2 = '(' + op2 + ')'
                stack.append(op2)
                priority[-1] = 3
            ops.append(c)
        elif c == '/':
            op2 = stack.pop()
            priority.pop()
            if len(op2) > 1 and op2[0] != '(':
                op2 = '(' + op2 + ')'
            stack.append(op2)
            priority.append(3)
            ops.append(c)
        else:
            stack.append(c)
            priority.append(3)
    
    ans = stack[0]
    for i in range(len(ops)):
        ans += ops[i] + stack[i + 1]
    
    return ans