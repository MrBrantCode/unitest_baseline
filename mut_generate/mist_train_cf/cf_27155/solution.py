"""
QUESTION:
Implement a function `calculate_license_bytes(license_text: str) -> int` that calculates the total number of bytes used by a Python package based on its license information, excluding comments and whitespace. The function should take the license text as input and return the total number of bytes used. Comments are denoted by a hash symbol (#) and extend to the end of the line. Whitespace includes spaces, tabs, and newline characters.
"""

def calculate_license_bytes(license_text: str) -> int:
    total_bytes = 0
    in_comment = False

    for char in license_text:
        if char == '#':
            in_comment = True
        elif char == '\n':
            in_comment = False
        elif not in_comment and not char.isspace():
            total_bytes += 1

    return total_bytes