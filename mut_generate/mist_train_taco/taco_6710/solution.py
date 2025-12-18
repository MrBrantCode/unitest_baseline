"""
QUESTION:
Write a function called calculate that takes 3 values. The first and third values are numbers. The second value is a character. If the character is "+" , "-", "*", or "/", the function will return the result of the corresponding mathematical function on the two numbers. If the string is not one of the specified characters, the function should return null (throw an `ArgumentException` in C#).

Keep in mind, you cannot divide by zero. If an attempt to divide by zero is made, return null (throw an `ArgumentException` in C#)/(None in Python).
"""

def calculate(num1, operation, num2):
    if operation not in ["+", "-", "*", "/"]:
        return None
    
    if operation == "/" and num2 == 0:
        return None
    
    try:
        return eval(f'{num1} {operation} {num2}')
    except (ZeroDivisionError, SyntaxError):
        return None