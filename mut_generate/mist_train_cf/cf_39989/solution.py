"""
QUESTION:
Create a function `count_package_dependencies` that takes a list of package names as input and returns a dictionary where the keys are the unique package names and the values are the counts of each package in the input list. The function should not modify the input list and should be able to handle a list of any length.

The input is a list of strings, where each string represents a package name. The output should be a dictionary where the keys are the unique package names and the values are the counts of each package. The function should return a new dictionary object.
"""

from typing import List, Dict

def count_package_dependencies(dependencies: List[str]) -> Dict[str, int]:
    package_count = {}
    for package in dependencies:
        if package in package_count:
            package_count[package] += 1
        else:
            package_count[package] = 1
    return package_count