"""
QUESTION:
Write a function `count_lines_of_code(code)` that counts the number of lines of code in a given string `code`, excluding empty lines and comments. The function should handle nested comments and inline comments. Nested comments are represented by starting and ending comment delimiters on separate lines, and inline comments start with a "#" character and continue until the end of the line. The function should consider comments as part of the code for the purpose of counting lines, but exclude inline comments from the line count. The function should have a time complexity of O(N), where N is the number of characters in the code.
"""

def count_lines_of_code(code):
    lines_of_code = 0
    is_comment = False

    for line in code.split("\n"):
        line = line.strip()

        if line == "":
            continue

        if line.startswith("#"):
            continue

        if line.startswith('"""') or line.startswith("'''"):
            if is_comment:
                is_comment = False
            else:
                is_comment = True
            continue

        if "#" in line:
            line = line.split("#")[0].strip()

        if line != "" and not is_comment:
            lines_of_code += 1

    return lines_of_code