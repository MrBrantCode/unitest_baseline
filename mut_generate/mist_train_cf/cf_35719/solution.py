"""
QUESTION:
Write a function `compareVersions(version1: str, version2: str) -> int` that compares two software version numbers in the format "major.minor.patch.build" where each component is an integer. The function should return 1 if `version1` is greater than `version2`, -1 if `version1` is less than `version2`, and 0 if `version1` is equal to `version2`. The comparison should follow the standard rules for version comparison, where a higher major version is considered greater, and if major versions are equal, the comparison proceeds to the minor version, and so on.
"""

def compareVersions(version1: str, version2: str) -> int:
    v1_components = list(map(int, version1.split('.')))
    v2_components = list(map(int, version2.split('.')))

    while len(v1_components) < 4:
        v1_components.append(0)
    while len(v2_components) < 4:
        v2_components.append(0)

    for i in range(4):
        if v1_components[i] > v2_components[i]:
            return 1
        elif v1_components[i] < v2_components[i]:
            return -1

    return 0