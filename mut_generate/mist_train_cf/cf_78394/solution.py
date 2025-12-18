"""
QUESTION:
Create a command-line interface (CLI) in Python with a `calculate` function that performs basic arithmetic operations and an `exit` function to quit the application. The `calculate` function should take three arguments in the format `[num1] [operation] [num2]` and support addition, subtraction, multiplication, and division operations. The CLI should guide the user by displaying the correct syntax and handling incorrect inputs. Implement this using the `cmd` module in Python.
"""

def calculate(arg):
    'Syntax: calculate [num1] [operation] [num2]\nPerforms calculation based on given arguments.'
    args = arg.split()
    if len(args) != 3:
        print("Please provide correct number of arguments")
        return
    
    num1, operator, num2 = args
    num1, num2 = float(num1), float(num2)
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
    else:
        print("Unsupported operation!")