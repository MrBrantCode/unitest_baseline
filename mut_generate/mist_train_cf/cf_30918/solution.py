"""
QUESTION:
Implement a function `extract_package_name` that takes a string `code` as input, representing a code snippet written in Japanese, and returns the package name enclosed within double quotes, which is followed by the comment "のテストコード群パッケージです。" The code snippet length is between 1 and 1000 characters, and the function should return an empty string if the package name is not found.
"""

import re

def extract_package_name(code: str) -> str:
    pattern = r'"(.*?)"のテストコード群パッケージです。'
    match = re.search(pattern, code)
    if match:
        return match.group(1)
    else:
        return ""