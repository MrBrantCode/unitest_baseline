"""
QUESTION:
Write a function process_version_control_output that takes a string output representing the version control system's output and returns a summary of the changes made to the files. The output string is composed of operations separated by commas, where each operation starts with 'added', 'modified', 'renamed', 'deleted', or 'untracked' followed by the file name(s). The function should return a string in the following format:
```
Added: [list of added files]
Modified: [list of modified files]
Renamed: [list of renamed files]
Deleted: [list of deleted files]
Untracked: [list of untracked files]
```
Note that the function may assume the input string is always valid.
"""

def process_version_control_output(output: str) -> str:
    added_files = []
    modified_files = []
    renamed_files = []
    deleted_files = []
    untracked_files = []

    operations = output.split(', ')
    for operation in operations:
        if operation.startswith('added'):
            added_files.append(operation.split(' ')[1])
        elif operation.startswith('modified'):
            modified_files.extend(operation.split(' ')[1:])
        elif operation.startswith('renamed'):
            renamed_files.extend(operation.split(' ')[1:])
        elif operation.startswith('deleted'):
            deleted_files.extend(operation.split(' ')[1:])
        elif operation.startswith('untracked'):
            untracked_files.extend(operation.split(' ')[1:])

    summary = f"Added: {added_files}\nModified: {modified_files}\nRenamed: {renamed_files}\nDeleted: {deleted_files}\nUntracked: {untracked_files}"
    return summary