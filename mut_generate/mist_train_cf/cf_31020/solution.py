"""
QUESTION:
Implement the `handle_directory` function, which takes two parameters: `base` (string) representing the base directory path and `is_dir` (boolean) indicating whether the base path is a directory. 

If `is_dir` is `True`, the function should attempt to list the files in the directory using `os.listdir(base)`. If the directory does not exist or is not accessible, raise a custom `NoSuchDir` exception with the message "The dir {0} does not exist". If any other OSError occurs during file listing, re-raise the exception. If `is_dir` is `False`, the function should return without raising any exceptions.
"""

import os
import errno

class NoSuchDir(Exception):
    pass

def handle_directory(base, is_dir):
    if is_dir:
        try:
            files = os.listdir(base)
        except OSError as e:
            if e.errno in (errno.ENOTDIR, errno.ENOENT):
                raise NoSuchDir('The dir {0} does not exist'.format(base))
            else:
                raise
    else:
        return