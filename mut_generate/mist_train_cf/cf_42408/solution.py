"""
QUESTION:
Implement a function `manipulate_lines(lines, max_length)` that takes a list of strings and an integer as input, and returns the final state of the list after left-justifying each line to the `max_length` if its length is less than `max_length`, and adding an empty line at the end if necessary.
"""

from typing import List

def manipulate_lines(lines: List[str], max_length: int) -> List[str]:
    cursor = 0
    for i, line in enumerate(lines):
        if len(line) < max_length:
            lines[i] = line.ljust(max_length)
            cursor = i + 1
        else:
            cursor = len(lines)
    
    if cursor < len(lines):
        line = ' ' * max_length
        try:
            lines[cursor] += line
        except IndexError:
            lines.append(line)
        cursor += 1
    
    return lines