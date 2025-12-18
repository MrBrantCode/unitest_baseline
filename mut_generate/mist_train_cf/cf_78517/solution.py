"""
QUESTION:
Create a function `calculate(s: str) -> int` that evaluates a valid expression string `s` containing non-negative integers, operators `+`, `-`, `*`, `/`, and parentheses `(`, `)`. The division of integers should be truncated towards zero. All intermediate results will fall within the range of `[-231, 231 - 1]`. The length of `s` will be between `1` and `104` inclusive. Do not use built-in library functions.
"""

def calculate(s: str) -> int:
    stack = []
    sign = '+'
    num = 0
    i = 0

    while i < len(s):
        c = s[i]
        if c.isdigit():
            num = num * 10 + int(c)
        if c == '(':
            j = i
            count = 0
            while i < len(s):
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                if count == 0:
                    break
                i += 1
            num = calculate(s[j+1:i])
            i += 1
        if (not c.isdigit() and c != ' ' and c != '(') or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            if sign == '-':
                stack.append(-num)
            if sign == '*':
                stack.append(stack.pop() * num)
            if sign == '/':
                stack.append(int(stack.pop() / num))
            num = 0
            if i < len(s):
                sign = c
        i += 1

    return sum(stack)