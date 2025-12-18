"""
QUESTION:
Write a function `count_lines_of_code(code)` to count the number of lines of code in a given string `code`, excluding empty lines and comments. The function should handle nested comments and inline comments. A nested comment is represented by starting and ending comment delimiters on separate lines, and an inline comment starts with a "#" character and continues until the end of the line. The function should consider the comments as part of the code for the purpose of counting lines and should have a time complexity of O(N), where N is the number of characters in the code.
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