"""
QUESTION:
Create a function `find_syntax_errors(code_snippets: List[str]) -> List[int]` that takes a list of strings representing Python code snippets as input and returns a list of line numbers (1-indexed) where syntax errors occur. The input list contains between 1 and 100 code snippets. If there are no syntax errors, return an empty list.
"""

from typing import List
import ast

def find_syntax_errors(code_snippets: List[str]) -> List[int]:
    error_lines = []
    for i, code in enumerate(code_snippets, start=1):
        try:
            ast.parse(code)
        except SyntaxError:
            error_lines.append(i)
    return error_lines