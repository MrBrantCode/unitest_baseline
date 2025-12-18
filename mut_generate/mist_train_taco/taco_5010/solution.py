"""
QUESTION:
Given a string s which represent an expression, evaluate this expression.
Integer division should truncate towards zero.
 
Example 1:
Input: s = "10*20+10"
Output: 210
Example 2:
Input: s = "16*5-5/15"
Output: 80
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function calculate() which takes s as input parameter and returns the value of the expression.
 
Expected Time Compelxity: O(|s|)
Expected Space Complexity: O(1)
 
Constraints:
1 <= |s| <= 10^{5}
^{s is a valid expression.}
Note: The answer is guaranteed to fit in a 32-bit integer.
"""

def evaluate_expression(s: str) -> int:
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isoperator(ch: str) -> bool:
        return ch in priority

    def infix_postfix(s: str) -> str:
        n = len(s)
        exp = ''
        stack = []
        i = 0
        while i < n:
            temp = ''
            while i < n and s[i].isnumeric():
                temp += s[i]
                i += 1
            exp += temp + '_'
            while i < n and len(stack) != 0 and (priority[stack[-1]] >= priority[s[i]]):
                exp += stack.pop()
            if i < n:
                stack.append(s[i])
            i += 1
        while len(stack) != 0:
            exp += stack.pop()
        return exp

    def calculation(s: str) -> int:
        n = len(s)
        stack = []
        i = 0
        while i < n:
            temp = ''
            while i < n and s[i].isnumeric():
                temp += s[i]
                i += 1
            if i < n and len(stack) > 1 and isoperator(s[i]):
                a = stack.pop()
                b = stack.pop()
                if s[i] == '+':
                    res = a + b
                if s[i] == '-':
                    res = b - a
                if s[i] == '*':
                    res = a * b
                if s[i] == '/':
                    res = b // a
                if s[i] == '^':
                    res = a ** b
                stack.append(res)
            else:
                stack.append(int(temp))
            i += 1
        return stack[-1]

    exp = infix_postfix(s)
    res = calculation(exp)
    return res