"""
QUESTION:
Create a function `count_program_units` that takes a string `cobol_code` representing COBOL source code as input and returns a dictionary containing unique program unit names (case-insensitive) as keys and their respective counts as values. The function should recognize program units in the format of a word or words (separated by hyphens) followed by 'DIVISION', 'SECTION', or 'PARAGRAPH'.
"""

import re

def count_program_units(cobol_code):
    program_units = {}
    pattern = r'(?<!-)\b[A-Z]+(?:-[A-Z]+)*(?:\s+DIVISION|\s+SECTION|\s+PARAGRAPH)\b'
    matches = re.findall(pattern, cobol_code, re.IGNORECASE)

    for match in matches:
        program_unit = match.strip().upper()
        program_units[program_unit] = program_units.get(program_unit, 0) + 1

    return program_units