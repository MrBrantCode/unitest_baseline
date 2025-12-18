"""
QUESTION:
Create a function `process_code_snippet(code: str, file_path: str) -> Tuple[str, str]` that takes a given code snippet as a string `code` and a file path as a string `file_path` as input. The function should extract the code description denoted by a Markdown heading (`##`) if present, otherwise use the file path as the code description, and the line-numbered snippet by numbering each line of the code snippet. The function should return a tuple containing the extracted code description and the line-numbered snippet.
"""

from typing import Tuple

def process_code_snippet(code: str, file_path: str) -> Tuple[str, str]:
    lines = code.split('\n')
    code_desc = file_path
    line_numbered_snippet = ''
    for i, line in enumerate(lines, start=1):
        line_numbered_snippet += f"{i}. {line}\n"
        if line.strip().startswith('##'):
            code_desc = line.strip().lstrip('#').strip()
    return code_desc, line_numbered_snippet