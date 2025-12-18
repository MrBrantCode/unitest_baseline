"""
QUESTION:
Write a function named `parse_code_metadata` that takes a string `code_snippet` as input and returns a tuple of two integers. The function should extract the code length and execution time from the code snippet. The code snippet will always contain comments in the format "// <Japanese text> : <value>", and the code length and execution time will always be integers.
"""

from typing import Tuple

def parse_code_metadata(code_snippet: str) -> Tuple[int, int]:
    code_length = 0
    execution_time = 0
    lines = code_snippet.split('\n')
    for line in lines:
        if "コード長" in line:
            code_length = int(line.split(":")[1].strip())
        elif "実行時間" in line:
            execution_time = int(line.split(":")[1].strip())
    return code_length, execution_time