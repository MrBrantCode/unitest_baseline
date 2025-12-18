"""
QUESTION:
One very experienced problem writer decided to prepare a problem for April Fools Day contest. The task was very simple - given an arithmetic expression, return the result of evaluating this expression. However, looks like there is a bug in the reference solution...


-----Input-----

The only line of input data contains the arithmetic expression. The expression will contain between 2 and 10 operands, separated with arithmetic signs plus and/or minus. Each operand will be an integer between 0 and 255, inclusive.


-----Output-----

Reproduce the output of the reference solution, including the bug.


-----Examples-----
Input
8-7+6-5+4-3+2-1-0

Output
4

Input
2+2

Output
-46

Input
112-37

Output
375
"""

def evaluate_april_fools_expression(expression: str) -> int:
    val = eval(expression)
    for i in range(len(expression)):
        if expression[i] == '+':
            j = i + 1
            c = -5
            while j < len(expression) and expression[j] != '+' and (expression[j] != '-'):
                c *= 10
                j += 1
            val += c
        elif expression[i] == '-':
            j = i + 1
            c = 3
            while j < len(expression) and expression[j] != '+' and (expression[j] != '-'):
                c *= 10
                j += 1
            val += c
    return val