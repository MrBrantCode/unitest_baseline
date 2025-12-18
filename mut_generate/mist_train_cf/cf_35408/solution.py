"""
QUESTION:
Create a function named `bump_version` that takes two parameters: `current_version` (a string representing the current version number in the format "major.minor.patch") and `bump_type` (a string representing the type of version bump to perform, which can be "major", "minor", or "patch"). The function should increment the corresponding version number based on the `bump_type` and return the updated version number as a string. If `bump_type` is not one of the specified options, the function should return "Invalid input".
"""

def bump_version(current_version, bump_type):
    version_numbers = current_version.split('.')
    
    if bump_type == "major":
        version_numbers[0] = str(int(version_numbers[0]) + 1)
        version_numbers[1] = "0"
        version_numbers[2] = "0"
    elif bump_type == "minor":
        version_numbers[1] = str(int(version_numbers[1]) + 1)
        version_numbers[2] = "0"
    elif bump_type == "patch":
        version_numbers[2] = str(int(version_numbers[2]) + 1)
    else:
        return "Invalid input"
    
    return '.'.join(version_numbers)