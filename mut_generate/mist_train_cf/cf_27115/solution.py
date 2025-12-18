"""
QUESTION:
Implement the `scan_dir_tree` method that recursively scans a directory tree and returns a dictionary containing information about the directory structure. The method should handle both regular and demo modes, where demo mode returns a subset of the directory information. The method takes in the following parameters:

- `dir_tree`: a list of directories and files in the current folder
- `cur_folder`: the current folder being scanned
- `path`: the path of the current folder
- `parent`: the parent directory of the current folder (optional)
- `demo`: a boolean flag indicating whether the method should run in demo mode (default is False)

The method should return a dictionary containing the directory information, including the current folder, path, and contents. In demo mode, it should only include subdirectory contents if the number of items in the subdirectory does not exceed 3.
"""

def scan_dir_tree(dir_tree, cur_folder, path, parent=None, demo=False):
    context = {'cur_folder': cur_folder, 'path': path, 'contents': []}

    for item in dir_tree:
        if isinstance(item, str):  # File
            context['contents'].append(item)
        elif isinstance(item, list):  # Subdirectory
            sub_folder = item[0]
            sub_path = f"{path}/{sub_folder}" if path else sub_folder
            sub_context = scan_dir_tree(item[1], sub_folder, sub_path, cur_folder, demo)
            if not demo or (demo and len(sub_context['contents']) <= 3):
                context['contents'].append(sub_context)

    return context