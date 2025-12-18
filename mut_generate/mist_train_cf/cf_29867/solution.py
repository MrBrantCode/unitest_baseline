"""
QUESTION:
Write a Python function `parse_script(script)` that takes a string `script` as input, containing Python function definitions with comments. The function should return a dictionary where the keys are the function names and the values are the associated comments, stripped of leading and trailing whitespaces and excluding the function name itself. The function name should match Python's identifier syntax (letters, underscores, and digits, but not starting with a digit).
"""

import re

def parse_script(script):
    function_pattern = r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(\s*\):[^\"]*\"([^"]*)\"'
    functions = re.findall(function_pattern, script)
    return {func[0]: func[1].strip() for func in functions}