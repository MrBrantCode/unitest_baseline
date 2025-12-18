"""
QUESTION:
Implement a function `check_for_duplicate_file` that checks for duplicate file names in a package manifest. The function takes two parameters: `packageManifest` (a dictionary with a "Loose" key containing a dictionary of file names) and `relativeSourceFilePath` (the file name to be checked for duplicates). The function should return `True` if `relativeSourceFilePath` is a duplicate in the "Loose" section of the package manifest (case-insensitive comparison), and `False` otherwise.
"""

def check_for_duplicate_file(packageManifest, relativeSourceFilePath):
    return any(
        entryFileName.lower() == relativeSourceFilePath.lower() 
        for entryFileName in packageManifest["Loose"].keys()
    )