"""
QUESTION:
Write a function `changeDirectory(currentDir: str, inputDir: str) -> str` that takes two parameters:
- `currentDir` (string): A valid absolute path starting with a forward slash ('/') and does not end with a trailing slash.
- `inputDir` (string): A directory to change to, which can be an absolute path starting with a forward slash ('/') or a relative path not starting with a forward slash.

The function should return the updated current working directory after applying the changes based on the `inputDir`. The function should handle both absolute and relative paths correctly, considering the use of ".." to refer to the parent directory.
"""

def changeDirectory(currentDir: str, inputDir: str) -> str:
    if inputDir.startswith('/'):  # Absolute path
        return inputDir.rstrip('/')  # Remove trailing slash if present
    else:  # Relative path
        components = currentDir.split('/')
        components.extend(inputDir.split('/'))
        stack = []
        for comp in components:
            if comp == '..':
                if stack:
                    stack.pop()
            elif comp and comp != '.':
                stack.append(comp)
        return '/' + '/'.join(stack)