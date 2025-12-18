"""
QUESTION:
Create a function `get_package_version` that takes a package name as a string and returns the version number of the package using the `pkg_resources` module. If the package is not found, the function should return "Package not found".
"""

import pkg_resources

def get_package_version(package_name):
    try:
        version = pkg_resources.get_distribution(package_name).version
        return version
    except pkg_resources.DistributionNotFound:
        return "Package not found"