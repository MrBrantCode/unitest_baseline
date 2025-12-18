"""
QUESTION:
Write a function `compareVersion(version1, version2)` that compares two version numbers `version1` and `version2` and returns an integer indicating their order. The function should return -1 if `version1` is less than `version2`, 1 if `version1` is greater than `version2`, and 0 if they are equal. The version numbers are strings composed of one or more revisions separated by dots, where each revision is a non-empty string of digits that may include leading zeros. If a version number does not specify a revision at a particular index, it is treated as if the revision were 0. The revisions are compared in a left-to-right order, disregarding any leading zeros. The input strings are guaranteed to be valid version numbers.
"""

def compareVersion(version1, version2):
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    while v1 and v1[-1] == 0:
        v1.pop()
    while v2 and v2[-1] == 0:
        v2.pop()
    for i in range(max(len(v1), len(v2))):
        v1_val = v1[i] if i < len(v1) else 0
        v2_val = v2[i] if i < len(v2) else 0
        if v1_val < v2_val:
            return -1
        elif v1_val > v2_val:
            return 1
    return 0