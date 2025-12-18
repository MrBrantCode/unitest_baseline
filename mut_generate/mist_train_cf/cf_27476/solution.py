"""
QUESTION:
Implement a function `compareVersions(version1: str, version2: str) -> int` that compares two software version numbers. The version numbers are strings in the format "major.minor.patch.build", where each component is an integer. Compare the versions based on the following rules: 
- Compare the major version first, then the minor version, then the patch version, and finally the build version. 
- If the major, minor, and patch versions are equal, but the build version differs, the comparison should be based on the build version. 
The function should return an integer:
- 1 if version1 is greater than version2
- 0 if version1 is equal to version2
- -1 if version1 is less than version2
"""

def entrance(version1: str, version2: str) -> int:
    v1_components = list(map(int, version1.split('.')))
    v2_components = list(map(int, version2.split('.')))

    while len(v1_components) < 4:
        v1_components.append(0)
    while len(v2_components) < 4:
        v2_components.append(0)

    for v1, v2 in zip(v1_components, v2_components):
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1

    return 0