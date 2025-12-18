"""
QUESTION:
Implement a function `find_incomplete_functions(code_lines)` that takes a list of strings representing Python code lines and returns a list of tuples, each containing the line number and the name of the incomplete function definition. A function definition is considered incomplete if it starts with 'def', followed by a function name and an opening parenthesis, but does not end with a colon on the same line or the next line.
"""

from typing import List, Tuple

def find_incomplete_functions(code_lines: List[str]) -> List[Tuple[int, str]]:
    incomplete_functions = []
    for i, line in enumerate(code_lines):
        if line.strip().startswith("def ") and line.strip().endswith("("):
            function_name = line.strip().split("(")[0].split("def ")[1]
            if i < len(code_lines) - 1:
                next_line = code_lines[i + 1].strip()
                if not next_line.endswith(":"):
                    incomplete_functions.append((i + 1, function_name))
            else:
                incomplete_functions.append((i + 1, function_name))
    return incomplete_functions