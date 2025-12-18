"""
QUESTION:
Write a function `count_lines_of_code(code)` that takes a string of code as input and returns the number of lines of code, excluding empty lines and comments. The code may contain nested comments, represented by starting and ending comment delimiters on separate lines. The function should consider the comments as part of the code for the purpose of counting lines and have a time complexity of O(N), where N is the number of characters in the code.
"""

def count_lines_of_code(code):
    lines_of_code = 0
    comment_level = 0

    for line in code.split("\n"):
        line = line.strip()

        if line == "":
            continue

        if line.startswith("#"):
            continue

        if line.startswith('"""') or line.startswith("'''"):
            if comment_level > 0:
                continue
            else:
                comment_level += 1

        if line.endswith('"""') or line.endswith("'''"):
            if comment_level > 0:
                comment_level -= 1
                if comment_level == 0:
                    lines_of_code += 1
                continue

        if comment_level == 0:
            lines_of_code += 1

    return lines_of_code