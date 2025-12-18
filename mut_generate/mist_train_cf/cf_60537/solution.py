"""
QUESTION:
Create a function called `arithmetic_operation` that takes three arguments: two numbers (`num1` and `num2`) and an operator. Implement the function to perform basic arithmetic operations (addition, subtraction, multiplication, and division) based on the provided operator, handling division by zero errors and invalid operators.
"""

def arithmetic_operation(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid Operator."