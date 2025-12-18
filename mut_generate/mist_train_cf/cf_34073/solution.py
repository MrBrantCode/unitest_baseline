"""
QUESTION:
Write a function `count_license_comments` that takes a string representing source code as input and returns the count of occurrences of the phrases "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE" and "GNU General Public License" within comments. A comment is defined as any text enclosed within `##` at the beginning of a line or any text following a line that starts with `#`.
"""

def count_license_comments(source_code: str) -> int:
    lines = source_code.split('\n')
    count = 0
    in_comment = False

    for line in lines:
        if line.startswith('##'):
            if "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE" in line:
                count += 1
            if "GNU General Public License" in line:
                count += 1
        elif line.lstrip().startswith('##'):
            if "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE" in line.lstrip():
                count += 1
            if "GNU General Public License" in line.lstrip():
                count += 1
        elif line.lstrip().startswith('#'):
            in_comment = True
        elif in_comment and not line.lstrip().startswith('#'):
            in_comment = False

    return count