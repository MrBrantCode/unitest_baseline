"""
QUESTION:
Create a function `zip_directory(source_dir, output_zip, exclusions)` that takes a directory path `source_dir`, a zip file name `output_zip`, and a list of exclusion patterns `exclusions`, and returns `True` if the directory is successfully zipped with exclusions, and `False` otherwise. The function should exclude files or directories matching the patterns in `exclusions` from the zip file.
"""

import os
import zipfile
import fnmatch

def zip_directory(source_dir, output_zip, exclusions):
    try:
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    if not any(fnmatch.fnmatch(file_path, pattern) for pattern in exclusions):
                        zipf.write(file_path, os.path.relpath(file_path, source_dir))
            return True
    except Exception as e:
        print(f"Error zipping directory: {e}")
        return False