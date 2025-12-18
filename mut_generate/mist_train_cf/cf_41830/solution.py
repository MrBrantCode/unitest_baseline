"""
QUESTION:
Create a function called `add_library_to_path` that takes in three parameters: `base_dir`, `sub_dir`, and `library_name`. The function should construct the full path of a library by joining the `base_dir`, `sub_dir`, `library_name`, and the fixed subdirectories "python" and "lib" and the filename "pyspark.zip". Then, it should insert this library path into the system path for import. The function should return the updated system path. The function should not require any specific file or directory to exist.
"""

import os
import sys

def add_library_to_path(base_dir, sub_dir, library_name):
    library_path = os.path.join(base_dir, sub_dir, library_name, "python", "lib", "pyspark.zip")
    sys.path.insert(0, library_path)
    return sys.path