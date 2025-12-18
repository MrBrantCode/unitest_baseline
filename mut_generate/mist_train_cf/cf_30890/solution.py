"""
QUESTION:
Create a function `parse_comments(code: str) -> List[str]` that takes a string of Python code as input and returns a list of all the commented-out lines in the code. The function should consider both single-line comments (denoted by `#`) and multi-line comments (denoted by triple quotes `'''` or `"""`), and ignore any commented-out code within strings or within multi-line strings. The input code string is guaranteed to be 1 character or more and 10^5 characters or less in length.
"""

from typing import List

def parse_comments(code: str) -> List[str]:
    in_single_line_comment = False
    in_multi_line_comment = False
    result = []
    lines = code.split('\n')

    for line in lines:
        line = line.strip()

        if in_multi_line_comment:
            if "'''" in line or '"""' in line:
                in_multi_line_comment = False
            result.append(line)
        else:
            if line.startswith('#'):
                result.append(line)
            elif "'''" in line or '"""' in line:
                in_multi_line_comment = True
                result.append(line)

    return result