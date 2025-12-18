"""
QUESTION:
Create a function named `invoke_print_statements` that takes a string containing one or more Python print statements separated by newlines. The function should execute each print statement individually, capture the output, and return a list of strings representing the captured output in the same order as the print statements. The print statements may contain any valid Python code, including variables or values that need to be evaluated before printing.
"""

import io
import contextlib

def invoke_print_statements(string):
    output = []
    
    # Split the string into individual print statements
    statements = string.strip().split('\n')
    
    # Iterate through each print statement
    for statement in statements:
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            # Execute the print statement and capture the output
            exec(statement)
            captured_output = buf.getvalue().strip()
            output.append(captured_output)
    
    return output