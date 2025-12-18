"""
QUESTION:
Create a function named `foo` that accepts a string `op` and an arbitrary number of arguments. The function should perform the operation specified by `op` on the provided numbers. `op` can be one of four operations: addition (`'+'`), subtraction (`'-'`), multiplication (`'*'`), or division (`'/'`). The function must handle edge cases, such as division by zero, and return an error message in such scenarios. Additionally, the function should check if at least two numbers are provided and return an error message if not.
"""

def foo(op, *args):
    if len(args) < 2:
        return "Requires at least two arguments"
    if op == '+':
        return sum(args)
    elif op == '-':
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif op == '*':
        result = args[0]
        for num in args[1:]:
            result *= num
        return result
    elif op == '/':
        try:
            result = args[0]
            for num in args[1:]:
                result /= num
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
    else:
        return "Invalid operation"