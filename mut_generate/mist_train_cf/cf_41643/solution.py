"""
QUESTION:
Create a function `bump_version` that takes two parameters: `current_version` (a string in the format "x.y.z" where x, y, and z are integers) and `part` (an integer representing the part of the version to bump, where 0 increments the major version, 1 increments the minor version, and 2 increments the patch version). The function should return the updated version as a string in the same format.
"""

def bump_version(current_version, part):
    major, minor, patch = map(int, current_version.split('.'))
    if part == 0:
        major += 1
        minor = 0
        patch = 0
    elif part == 1:
        minor += 1
        patch = 0
    elif part == 2:
        patch += 1
    return f"{major}.{minor}.{patch}"