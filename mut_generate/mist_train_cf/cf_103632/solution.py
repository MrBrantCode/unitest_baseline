"""
QUESTION:
Write a function called `update_folder` that generates a Unix command to copy files from a specified source folder to a destination folder, only including files that have been modified within the last 24 hours.
"""

def update_folder(src_folder, dst_folder):
    """
    Generates a Unix command to copy files from a specified source folder to a destination folder,
    only including files that have been modified within the last 24 hours.

    Args:
        src_folder (str): Path to the source folder.
        dst_folder (str): Path to the destination folder.

    Returns:
        str: A Unix command to copy the modified files.
    """
    command = f"find {src_folder} -type f -mtime -1 -exec cp {{}} {dst_folder} \\;"
    return command