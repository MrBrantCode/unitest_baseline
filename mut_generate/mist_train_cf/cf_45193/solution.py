"""
QUESTION:
Implement a simple compiler function named `compile` in Python that takes a string of basic arithmetic operations as input, where operations are separated by whitespace. The input string can contain 'ADD', 'SUB', and integers. The function should interpret the operations and return the result. The operations should be executed from left to right.
"""

def compile(code):
    """
    This function compiles a string of basic arithmetic operations.
    
    It takes a string of operations as input, where operations are separated by whitespace.
    The input string can contain 'ADD', 'SUB', and integers.
    The function interprets the operations and returns the result.
    
    The operations are executed from left to right.
    
    Parameters:
    code (str): A string of basic arithmetic operations.
    
    Returns:
    int: The result of the operations.
    """
    operations = code.split(' ')
    current_operation = ''
    sum = 0
    for operation in operations:
        if operation == 'ADD' or operation == 'SUB':
            current_operation = operation
        else:
            if current_operation == 'ADD':
                sum += int(operation)
            elif current_operation == 'SUB':
                sum -= int(operation)
            else:
                sum = int(operation)
    return sum