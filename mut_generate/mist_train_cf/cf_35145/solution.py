"""
QUESTION:
Write a function `check_python_compatibility(package_name, python_versions)` where:
- `package_name` is the name of the Python package to be analyzed.
- `python_versions` is a list of strings containing the Python versions to be checked for compatibility.

The function should return a tuple of two lists:
1. A list of Python versions that are compatible with the given package.
2. A list of Python versions that are incompatible with the given package.

A package is considered compatible with a Python version if it specifies that version in its compatibility metadata.
"""

def entrance(package_name, python_versions):
    compatible_versions = []
    incompatible_versions = []

    package_metadata = [
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]  # Replace this with actual package metadata retrieval logic

    for version in python_versions:
        if f'Programming Language :: Python :: {version}' in package_metadata:
            compatible_versions.append(version)
        else:
            incompatible_versions.append(version)

    return compatible_versions, incompatible_versions