"""
QUESTION:
Write a function named `resolve_merge_conflict` that takes in two string parameters, `current_branch` and `merge_branch`, both representing different versions of a code file with a conflict marked by `<<<<<<<`, `=======`, and `>>>>>>>` markers. The function should return a string representing the resolved conflict, with the conflict markers removed, and the conflicted lines replaced with the version from the current branch, the version from the merge branch, or a completely new version. Assume that the conflict markers are correctly formatted and that there is only one conflict in the file.
"""

def resolve_merge_conflict(current_branch, merge_branch):
    current_lines = current_branch.split('\n')
    merge_lines = merge_branch.split('\n')
    
    conflict_start = False
    conflict_end = False
    resolved_lines = []
    
    for line in current_lines:
        if line.startswith('<<<<<<<'):
            conflict_start = True
            continue
        elif line.startswith('======='):
            conflict_end = True
        elif line.startswith('>>>>>>>'):
            conflict_end = False
            continue
        elif conflict_end:
            resolved_lines.append(line)
        else:
            resolved_lines.append(line)
            
    return '\n'.join(resolved_lines)