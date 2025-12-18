"""
QUESTION:
Write a function `highestVersion` that takes a list of strings `licenses` as input, where each string contains a license name and a positive integer version separated by a space. The function should return a list of strings representing the highest version of each unique license name. If multiple licenses have the same name and highest version, only the first occurrence should be included in the result.
"""

from typing import List

def highestVersion(licenses: List[str]) -> List[str]:
    license_versions = {}
    for license in licenses:
        name, version = license.rsplit(' ', 1)
        version = float(version)
        if name not in license_versions or version > license_versions[name]:
            license_versions[name] = version
    return [f"{name} {version}" for name, version in license_versions.items()]