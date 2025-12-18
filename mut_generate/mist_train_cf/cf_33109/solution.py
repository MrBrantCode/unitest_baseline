"""
QUESTION:
Create a function `which(program)` that locates a program in the system's PATH. The function should take the name of a program as input and return the full path to the program if it exists, or `None` if it is not found. The function should handle both Windows and non-Windows systems, and should check if the found file is executable. If the system is Windows, the function should also check if the program exists with a `.exe` extension.
"""

import os
import stat
import sys

def which(program):
    def is_executable_file(path):
        return os.path.isfile(path) and os.access(path, os.X_OK)

    def search_path(program):
        path_dirs = os.environ["PATH"].split(os.pathsep)
        for path_dir in path_dirs:
            exe_file = os.path.join(path_dir, program)
            if is_executable_file(exe_file):
                return exe_file
        return None

    if sys.platform == "win32":
        if os.path.isfile(program) and is_executable_file(program):
            return program
        else:
            return search_path(program + ".exe")
    else:
        return search_path(program)