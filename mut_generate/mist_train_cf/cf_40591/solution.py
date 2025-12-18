"""
QUESTION:
Implement a function `cd_command(root, path)` that simulates the `cd` command in a file system. The function should change the current directory to the specified path and print the new working directory. The path can be absolute (starting from the root directory) or relative to the current directory. If the specified path is invalid, the function should print "No such file or directory". The function should handle the '..' notation to navigate to the parent directory. The file system is represented as a tree structure where each node represents a directory and its children represent files or subdirectories.
"""

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

def cd_command(root, path):
    """
    Simulates the cd command in a file system.

    Args:
    root (TreeNode): The root directory of the file system.
    path (str): The path to navigate to.

    Returns:
    None
    """
    if path.startswith('/'):
        current = root
        path = path[1:]
    else:
        current = root

    directories = path.split('/')
    for directory in directories:
        if directory == '..':
            if hasattr(current, 'parent') and current.parent:
                current = current.parent
        elif directory:
            found = False
            for child in current.children:
                if child.name == directory:
                    child.parent = current
                    current = child
                    found = True
                    break
            if not found:
                print("No such file or directory")
                return

    print('/' + '/'.join(d.name for d in get_path(current)))

def get_path(node):
    path = []
    while node:
        path.insert(0, node)
        node = node.parent if hasattr(node, 'parent') else None
    return path