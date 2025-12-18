"""
QUESTION:
Create a function `compare_versions(version1: str, version2: str) -> int` that compares two version strings in semantic versioning format (three non-negative integers separated by periods, optionally followed by a pre-release identifier). The function should return:
- 1 if `version1` is greater than `version2`
- -1 if `version1` is less than `version2`
- 0 if `version1` is equal to `version2`

The comparison rules are as follows: 
1. Compare the numeric parts (major, minor, and patch) of the version strings. If any part of `version1` is greater than the corresponding part of `version2`, return 1; if it is less, return -1.
2. If the numeric parts are equal, compare the pre-release identifiers. If one version has a pre-release identifier and the other does not, the one without the pre-release identifier is considered greater.
"""

def entrance(version1: str, version2: str) -> int:
    v1_parts = version1.split('-')[0].split('.')
    v2_parts = version2.split('-')[0].split('.')

    for i in range(3):
        if int(v1_parts[i]) > int(v2_parts[i]):
            return 1
        elif int(v1_parts[i]) < int(v2_parts[i]):
            return -1

    if len(version1.split('-')) > 1 and len(version2.split('-')) == 1:
        return -1
    elif len(version1.split('-')) == 1 and len(version2.split('-')) > 1:
        return 1
    elif len(version1.split('-')) > 1 and len(version2.split('-')) > 1:
        pre_release1 = version1.split('-')[1]
        pre_release2 = version2.split('-')[1]
        if pre_release1 < pre_release2:
            return -1
        elif pre_release1 > pre_release2:
            return 1

    return 0