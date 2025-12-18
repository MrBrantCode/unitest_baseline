"""
QUESTION:
Write a function `compare_versions(version1: str, version2: str) -> int` that compares two non-empty version numbers represented as strings, which contain only digits and the '.' character. The function should return:
- 1 if `version1` is greater than `version2`
- -1 if `version1` is smaller than `version2`
- 0 if `version1` is equal to `version2`

The comparison should follow the standard lexicographical ordering.
"""

def entrance(version1: str, version2: str) -> int:
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))

    # Make the version lists equal in length by appending zeros
    while len(v1) < len(v2):
        v1.append(0)
    while len(v2) < len(v1):
        v2.append(0)

    # Compare each segment of the version numbers
    for i in range(len(v1)):
        if v1[i] > v2[i]:
            return 1
        elif v1[i] < v2[i]:
            return -1

    return 0  # Both versions are equal