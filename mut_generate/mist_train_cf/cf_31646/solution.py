"""
QUESTION:
Implement a function `interpret_code` that takes a list of code lines as input and returns a dictionary representing the memory state. The function should iterate through the code lines, and for each line, if the line contains only digits, it should convert the line to an integer and store it in the memory dictionary at the corresponding index; otherwise, it should store the line as a string in the memory dictionary at the corresponding index. The memory dictionary should use the line index as the key.
"""

import re

def interpret_code(code_lines):
    memory = {}
    for index, line in enumerate(code_lines):
        line = line.rstrip("\n")
        if re.match(r'^\d+$', line):
            memory[index] = int(line)
        else:
            memory[index] = line
    return memory