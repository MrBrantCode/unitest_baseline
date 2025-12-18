"""
QUESTION:
Implement a function `find_template_files(base_directory)` that takes a base directory path as input and returns a list of template file names found within the directory and its subdirectories. The function should consider all files within the "content/template" subdirectory as template files. It should exclude hidden files and directories from the search. The returned file names should be relative to the base directory.
"""

import os

def find_template_files(base_directory):
    template_files = []

    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file.startswith('.') or file.startswith('__'):
                continue  # Skip hidden files and directories
            if os.path.basename(root) == 'template' and os.path.basename(os.path.dirname(root)) == 'content':
                template_files.append(os.path.relpath(os.path.join(root, file), base_directory))

    return template_files