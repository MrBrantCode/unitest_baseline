"""
QUESTION:
Implement a Python function `count_leading_spaces` that takes a list of strings representing code lines as input and returns a list of integers representing the number of leading spaces or tabs in each non-empty line. The function should ignore empty lines and consider both spaces and tabs as one unit of indentation.
"""

from typing import List

def count_leading_spaces(code_lines: List[str]) -> List[int]:
    indentslist = []
    for line in code_lines:
        if line.strip():  
            nindents = 0
            for char in line:
                if char == ' ' or char == '\t':
                    nindents += 1
                else:
                    break
            indentslist.append(nindents)
    return indentslist