"""
QUESTION:
Write a function `extractFunctionPrototypes(headerContent: str) -> List[str]` that takes a string representing the content of a C/C++ header file and returns a list of function prototypes found in the file. Function prototypes are defined as lines of code that start with a return type, followed by the function name, parameters, and ending with a semicolon.
"""

from typing import List
import re

def extractFunctionPrototypes(headerContent: str) -> List[str]:
    prototypes = re.findall(r'\b\w+\s+\w+\s*\([^;]*\);', headerContent)
    return prototypes