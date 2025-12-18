"""
QUESTION:
Implement a function named `extract_function_info` that takes a string of C header code as input and returns a dictionary where the keys are the function names and the values are lists of tuples, each containing the parameter name and type. The function should be able to parse the C header code and extract the function names, parameter names, and their types. The input string may contain comments, macro definitions, and other code, but the function should only extract information from function prototypes that match the pattern `extern void CL_API_ENTRY function_name(parameters);`.
"""

import re

def extract_function_info(header_code):
    function_info = {}
    function_pattern = r'extern void CL_API_ENTRY (\w+)\((.*?)\);'
    matches = re.findall(function_pattern, header_code, re.DOTALL)
    
    for match in matches:
        function_name = match[0]
        parameters = match[1].split(',')
        param_info = []
        for param in parameters:
            param = param.strip()
            if param:
                param_type, param_name = param.rsplit(' ', 1)
                param_info.append((param_name, param_type))
        function_info[function_name] = param_info
    
    return function_info