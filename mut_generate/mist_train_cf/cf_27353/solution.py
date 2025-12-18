"""
QUESTION:
Implement the function `simplify_path(path: str) -> str` to simplify a Unix-style file path. The function should take a string representing the file path, replace consecutive multiple slashes with a single slash, remove any trailing slash, and resolve '.' and '..' in the path where '.' refers to the current directory and '..' refers to the parent directory. If there is no parent directory, '..' should refer to the root directory.
"""

def simplify_path(path: str) -> str:
    stack = []
    components = path.split('/')
    
    for component in components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if stack:
                stack.pop()
        else:
            stack.append(component)
    
    simplified_path = '/' + '/'.join(stack)
    return simplified_path