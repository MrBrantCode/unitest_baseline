"""
QUESTION:
Create a function `compare_versions(version1: str, version2: str) -> int` that takes two version strings as input, where each version string is a non-empty string consisting of one or more dot-separated numeric components with possible leading zeroes. The function should compare the version strings component by component from left to right, padding the shorter version with zeroes if necessary, and return 1 if `version1` is greater than `version2`, -1 if `version1` is less than `version2`, and 0 if `version1` is equal to `version2`.
"""

def entrance(version1: str, version2: str) -> int:
    v1_components = list(map(int, version1.split('.')))
    v2_components = list(map(int, version2.split('.')))

    # Pad the shorter version with zeroes
    max_len = max(len(v1_components), len(v2_components))
    v1_components += [0] * (max_len - len(v1_components))
    v2_components += [0] * (max_len - len(v2_components))

    for comp1, comp2 in zip(v1_components, v2_components):
        if comp1 > comp2:
            return 1
        elif comp1 < comp2:
            return -1

    return 0