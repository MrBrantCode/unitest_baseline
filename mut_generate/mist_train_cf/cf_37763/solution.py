"""
QUESTION:
Implement the function `filter_packages(packages, required_lib, optional_flag)` that takes in a list of dictionaries representing software packages, a required library name, and an optional flag. Each package dictionary contains the keys `name`, `libraries`, and `optional`. The function should return a list of package names that meet the following conditions: the package requires the specified `required_lib` and, if `optional_flag` is True, the package is optional, or if `optional_flag` is False, the package is not optional.
"""

from typing import List, Dict

def entrance(packages: List[Dict], required_lib: str, optional_flag: bool) -> List[str]:
    filtered_packages = []
    for package in packages:
        if required_lib in package['libraries'] and package['optional'] == optional_flag:
            filtered_packages.append(package['name'])
    return filtered_packages