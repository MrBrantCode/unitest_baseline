"""
QUESTION:
Write a function `extract_function_signature` that takes a string representing a code snippet as input and returns the function signature in a standard format. The code snippet defines a function using a custom syntax and includes the function name, input parameter(s), return type, and additional information. 

The function name is the first string after the `def` keyword, input parameter(s) are within the parentheses following the function name, and the return type is after the last comma within the parentheses. Additional information, if present, should be included in the function signature. The function should handle different function definitions following the same custom syntax and produce the corresponding function signatures.
"""

import re

def extract_function_signature(code_snippet):
    # Extract function name
    function_name = re.search(r'def\s+(\w+)\(', code_snippet).group(1)

    # Extract input parameter(s)
    input_params = re.search(r'\((.*?)\)', code_snippet).group(1)

    # Extract return type
    return_type = input_params.split(',')[-1].strip()

    # Extract additional information
    additional_info = code_snippet.split('(')[1].split(')')[0]

    # Output function signature
    return {
        "Name": function_name,
        "Input Parameter(s)": input_params,
        "Return Type": return_type,
        "Additional Information": additional_info
    }