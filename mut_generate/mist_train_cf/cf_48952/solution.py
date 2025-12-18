"""
QUESTION:
Write a function named `operation_test` that takes two variables `v1` and `v2` and an operation as input, identifies the data types of `v1` and `v2`, checks if the combination of variables is logically correct for the given operation, performs the operation, and handles any errors that might arise. The function should support addition, subtraction, multiplication, and division operations. Additionally, create a function named `data_type` that returns the data type of a given variable. The functions should handle edge cases such as division by zero and numerical operations with null values.
"""

def operation_test(v1, v2, operation):
    operations = ['+', '-', '*', '/']
    
    if operation not in operations:
        print("Unsupported operation")
        return
    try:   
        if operation == '+':
            result = v1 + v2
        elif operation == '-':
            result = v1 - v2
        elif operation == '*':
            result = v1 * v2
        elif operation == '/':
            result = v1 / v2
        print("Result: ", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except TypeError:
        print("Error: Unsupported operation for these data types")
        
def data_type(x):
    return type(x).__name__