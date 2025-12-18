"""
QUESTION:
Write a function `extract_license_text` that takes a string representing the content of a source file as input and returns the extracted license text. The input string will be in the form of a source code file with comments denoted by `#` at the beginning of the line for single-line comments and enclosed within `#` at the beginning and `#` at the end for multi-line comments. The function should handle both single-line and multi-line comments and extract the license text enclosed within them, excluding the comment delimiters.
"""

import re

def extract_license_text(source_code):
    multi_line_comment_pattern = r'#(.*?)#'
    single_line_comment_pattern = r'#(.*)'

    multi_line_matches = re.findall(multi_line_comment_pattern, source_code, re.DOTALL)
    if multi_line_matches:
        return multi_line_matches[0].strip()

    single_line_matches = re.findall(single_line_comment_pattern, source_code)
    for match in single_line_matches:
        if match.strip():
            return match.strip()

    return ""