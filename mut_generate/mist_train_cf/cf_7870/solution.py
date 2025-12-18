"""
QUESTION:
Write a function `isolate_comments(code, start_line, start_char, keyword)` that isolates comments in a given piece of code. The function should only consider comments that start with the specified character `start_char`, contain the specified `keyword`, and occur after the specified `start_line` (1-indexed). The function should return a list of the isolated comments.
"""

def isolate_comments(code, start_line, start_char, keyword):
    lines = code.split("\n")
    comments = []
    for line_num in range(start_line - 1, len(lines)):
        line = lines[line_num]
        if line.lstrip().startswith(start_char):
            comment = line.strip(start_char).strip()
            if keyword in comment:
                comments.append(comment)
    return comments