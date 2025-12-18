"""
QUESTION:
Implement a function `custom_normpath` that takes a string representing a file path as input and returns the normalized path. The normalized path should have the following characteristics:
- All empty components are replaced by a single empty component.
- All occurrences of ‘/./’ in the middle of a path are replaced by a single ‘/’.
- All occurrences of ‘/../’ in the middle of a path are replaced by the parent directory name.
The function should not use any built-in path normalization functions.
"""

def custom_normpath(path: str) -> str:
    components = path.split('/')
    stack = []
    for component in components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if stack and stack[-1] != '..':
                stack.pop()
            else:
                stack.append(component)
        else:
            stack.append(component)
    normalized_path = '/'.join(stack)
    if path.startswith('/'):
        return '/' + normalized_path
    else:
        return normalized_path