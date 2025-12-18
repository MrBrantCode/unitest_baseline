"""
QUESTION:
Write a function named `find_function_calls` that takes a string of Python code as input and returns a dictionary where the keys are function names and the values are the number of times each function is called in the code. The function should consider only explicit function calls (i.e., expressions with parentheses) and ignore any other code elements.
"""

def find_function_calls(code):
    function_calls = {}
    lines = code.split('\n')
    for line in lines:
        if '(' in line:
            function_name = line.split('(')[0].strip()
            if function_name in function_calls:
                function_calls[function_name] += 1
            else:
                function_calls[function_name] = 1
    return function_calls