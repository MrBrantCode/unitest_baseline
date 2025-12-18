"""
QUESTION:
Write a function `auto_increment_version` to auto-increment a version number for an asp.net application. The function should take the current version as a string in the format 'major.minor.patch' and return the incremented version as a string.
"""

def auto_increment_version(version):
    """
    Auto-increment a version number for an asp.net application.

    Args:
        version (str): The current version as a string in the format 'major.minor.patch'.

    Returns:
        str: The incremented version as a string.
    """
    major, minor, patch = map(int, version.split('.'))
    patch += 1
    if patch == 10:
        patch = 0
        minor += 1
        if minor == 10:
            minor = 0
            major += 1
    return f"{major}.{minor}.{patch}"