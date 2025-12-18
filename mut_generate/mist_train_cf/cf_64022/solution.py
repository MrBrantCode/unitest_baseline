"""
QUESTION:
Remove all sub-directories from a list of directories and return the remaining directories in any sequence. 

A sub-directory is defined as a directory that is situated within another directory, i.e., `directory[i]` is a sub-directory of `directory[j]` if `directory[i]` starts with `directory[j]`. 

The directory paths are in the form of one or more concatenated strings of the form: `/` followed by one or more lowercase English alphabets.

The function `removeSubfolders` takes a list of directories `folder` as input and returns the list of remaining directories after removing all sub-directories. 

Constraints: `1 <= len(folder) <= 4 * 10^4`, `2 <= len(folder[i]) <= 100`, `folder[i]` contains only lowercase letters and `/`, `folder[i]` always starts with `/`, and each directory name is unique.
"""

def removeSubfolders(folder):
    folder.sort()
    result=[]
    cur=None
    for f in folder:
        if cur is None or not f.startswith(cur):
            result.append(f)
            cur=f+"/"
    return result