"""
QUESTION:
Create a function `find_staged_files()` that takes the output of the `git diff --cached` command as a string, extracts the staged file names, and returns them as a list. The staged file names are those lines in the output that start with "diff --git". Each file name is the part of the line after " b/".
"""

def find_staged_files(git_diff_output):
    """
    Extracts staged file names from the output of the `git diff --cached` command.

    Args:
        git_diff_output (str): The output of the `git diff --cached` command.

    Returns:
        list: A list of staged file names.
    """
    staged_files = []
    for line in git_diff_output.split("\n"):
        if line.startswith("diff --git"):
            file = line.split(" b/")[1]
            staged_files.append(file)
    return staged_files