"""
QUESTION:
Implement a function `compare_versions(version1: str, version2: str) -> int` that compares two version strings in the semantic versioning format. The function should return 1 if `version1` is greater than `version2`, -1 if `version1` is lesser than `version2`, and 0 if `version1` is equal to `version2`. The version strings consist of three numeric components separated by periods and may contain a pre-release tag denoted by a hyphen followed by alphanumeric characters. Assume that the input version strings will always be valid and follow the semantic versioning format.
"""

def compare_versions(version1: str, version2: str) -> int:
    def parse_version(version: str) -> tuple:
        version_parts = version.split('-')
        main_version = version_parts[0].split('.')
        pre_release = version_parts[1] if len(version_parts) > 1 else None
        return tuple(map(int, main_version)), pre_release

    v1, pre1 = parse_version(version1)
    v2, pre2 = parse_version(version2)

    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        if pre1 and pre2:
            return 1 if pre1 > pre2 else (-1 if pre1 < pre2 else 0)
        elif pre1:
            return -1
        elif pre2:
            return 1
        else:
            return 0