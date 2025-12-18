"""
QUESTION:
Implement the `compare_versions(version1: str, version2: str) -> int` function. The function takes two version numbers as strings in the format "x.y.z", where x, y, and z are non-negative integers, and returns 1 if version1 is greater, -1 if version2 is greater, and 0 if they are equal.
"""

def compare_versions(version1: str, version2: str) -> int:
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))

    while len(v1) < len(v2):
        v1.append(0)
    while len(v2) < len(v1):
        v2.append(0)

    for i in range(len(v1)):
        if v1[i] > v2[i]:
            return 1
        elif v1[i] < v2[i]:
            return -1

    return 0