"""
QUESTION:
Implement the `resolve_path` function, which takes two arguments: `current_path` and `input_path`. The function should resolve the `input_path` relative to the `current_path` and return the final absolute path. The function must handle the special characters `.`, `..`, and `|`, representing the current directory, parent directory, and root directory, respectively. The input path can be either absolute (starting with `|`) or relative to the current directory.
"""

def resolve_path(current_path, input_path):
    if input_path.startswith('|'):
        current_path = '|'
        input_path = input_path[1:]

    paths = input_path.split('/')
    for path in paths:
        if path == '.':
            continue
        elif path == '..':
            if current_path != '|':
                current_path = current_path.rsplit('/', 1)[0]
        else:
            current_path = f"{current_path}/{path}"

    return current_path