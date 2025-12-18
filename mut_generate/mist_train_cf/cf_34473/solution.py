"""
QUESTION:
Implement a function `extractFunctionNames` that takes a string `sourceCode` containing C++ source code as input and returns a list of strings containing the names of all the functions present in the source code. A function name is defined as any valid C++ identifier followed by an opening parenthesis '('. The function should only return the function names and exclude any parameters or function bodies. The input string may contain multiple functions and other C++ syntax.
"""

from typing import List
import re

def extractFunctionNames(sourceCode: str) -> List[str]:
    function_names = re.findall(r'\b\w+\s*\([^)]*\)\s*{', sourceCode)
    function_names = [name.split('(')[0].strip() for name in function_names]
    return function_names