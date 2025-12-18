"""
QUESTION:
Write a function `count_lines_of_code(code)` to count the number of lines of code in a given string `code`, excluding empty lines and comments. The function should handle nested comments, which are represented by triple quotes on separate lines, and have a time complexity of O(N), where N is the number of characters in the `code`.
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