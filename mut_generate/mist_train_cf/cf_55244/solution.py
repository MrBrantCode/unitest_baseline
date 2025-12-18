"""
QUESTION:
Create a function named `calculate` that accepts a string representing an arithmetic expression with the format `num1 operator num2`. The function should perform the arithmetic operation based on the operator provided and return the result. The function should support the operators '+', '-', '*', and '/'. Implement error handling to handle invalid number inputs, division by zero, and invalid operators.
"""

def calculate(expression):
    expression = expression.split()

    try:
        num1 = float(expression[0])
        num2 = float(expression[2])
        operator = expression[1]
    except:
        return "Error: Invalid number input!"

    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2!=0:
                result = num1 / num2
            else:
                return "Error: Division by zero!"
        else:
            return "Error: Invalid operator!"
    except Exception as e:
        return str(e)

    return result