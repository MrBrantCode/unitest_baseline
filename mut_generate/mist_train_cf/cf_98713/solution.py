"""
QUESTION:
Write a function `compare_versions(v1, v2, max_length)` that compares two version numbers `v1` and `v2` in a case-insensitive manner and returns an integer indicating their relationship. The function should handle cases where the input versions have different numbers of sub-versions or different numbers of digits in each sub-version. If one version has more sub-versions than the other, assume the missing sub-versions to be zero. Similarly, if a sub-version has fewer digits than the other, assume the missing digits to be zero. The function should also ensure that the combined length of `v1` and `v2` does not exceed `max_length`. If the input string exceeds the maximum length, return -2. The function should return 1 if `v1` is greater than `v2`, -1 if `v1` is less than `v2`, and 0 if they are equal.
"""

def compare_versions(v1, v2, max_length):
    if len(v1+v2) > max_length:
        return -2

    v1 = v1.lower()
    v2 = v2.lower()

    v1_parts = v1.split('.')
    v2_parts = v2.split('.')

    max_parts = max(len(v1_parts), len(v2_parts))
    v1_parts += ['0'] * (max_parts - len(v1_parts))
    v2_parts += ['0'] * (max_parts - len(v2_parts))

    for v1_part, v2_part in zip(v1_parts, v2_parts):
        v1_subparts = v1_part.split('-')
        v2_subparts = v2_part.split('-')

        max_subparts = max(len(v1_subparts), len(v2_subparts))
        v1_subparts += ['0'] * (max_subparts - len(v1_subparts))
        v2_subparts += ['0'] * (max_subparts - len(v2_subparts))

        for v1_subpart, v2_subpart in zip(v1_subparts, v2_subparts):
            if int(v1_subpart) > int(v2_subpart):
                return 1
            elif int(v1_subpart) < int(v2_subpart):
                return -1

    return 0