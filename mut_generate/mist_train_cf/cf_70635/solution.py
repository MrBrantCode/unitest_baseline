"""
QUESTION:
Function Name: simplify_path

Given an absolute path in a Unix-style file system, convert it to the simplified canonical path. The path can contain periods (.) referring to the current directory and double periods (..) referring to the directory up a level. Any multiple consecutive slashes are treated as a single slash.

Restrictions:
- The path starts with a single slash (/).
- Any two directories are separated by a single slash (/).
- The path does not end with a trailing (/).
- The path only contains the directories on the path from the root directory to the target file or directory (no period (.) or double period (..)).
- The path length is between 1 and 3000 characters.
- The path consists of English letters, digits, period (.), slash (/), or underscore (_).
- The path is a valid absolute Unix path.
- Any other format of periods (e.g., ...) is considered an invalid path and should return "Invalid path".
"""

def simplify_path(path):
    stack = []
    for part in path.split("/"):
        if part == "..":
            if stack:
                stack.pop()
        elif part == "." or not part:
            continue
        elif part.find(".") != -1 and len(part) != part.count("."):
            return "Invalid path"
        else:
            stack.append(part)
    return "/" + "/".join(stack)