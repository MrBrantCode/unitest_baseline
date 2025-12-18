"""
QUESTION:
Create a function `parseBoolExpr(expression: str) -> bool` that evaluates a given boolean expression, represented as a string, and returns the result. The expression can contain the following elements: `t` (True), `f` (False), `!(expr)` (logical NOT of `expr`), `&(expr1,expr2,...)` (logical AND of two or more inner expressions), `|(expr1,expr2,...)` (logical OR of two or more inner expressions), and `^(expr1,expr2,...)` (logical XOR of two or more inner expressions). The input `expression` is guaranteed to be a valid boolean expression, with length between 1 and 20000, and consists only of characters in `{(' , ')', '&', '|', '!', 't', 'f', ',', '^'}`.
"""

def parseBoolExpr(expression: str) -> bool:
    stack = []
            
    def calc(op, Arr):
        if op == "&":
            return all(Arr)
        elif op == "|":
            return any(Arr)
        elif op == "^":
            return sum(Arr) % 2 == 1
        else:
            # this must be "!" operator
            return not Arr[0]
            
    for c in expression:
        if c == ')' :
            tmpList = []
            while stack[-1] != "(":
                tmpList.append(stack.pop())
            stack.pop()   # pop "("
            op = stack.pop()
            res = calc(op, tmpList)
            stack.append(res)
        elif c != ",":
            if c == "f":
                stack.append(False)
            elif c == "t":
                stack.append(True)
            else: 
                stack.append(c)
    return stack[0]