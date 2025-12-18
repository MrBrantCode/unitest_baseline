"""
QUESTION:
Write a function `compare_versions(v1, v2, max_length)` that compares two version strings `v1` and `v2` in a case-insensitive manner and returns an integer value indicating their order. The function should handle cases where the input versions have different numbers of sub-versions or different numbers of digits in each sub-version. If one version has more sub-versions than the other, assume the missing sub-versions to be zero. If a sub-version has fewer digits than the other, assume the missing digits to be zero. The function should also check if the combined length of `v1` and `v2` exceeds `max_length` and return -2 if it does. The function should return 1 if `v1` is greater than `v2`, -1 if `v1` is less than `v2`, and 0 if `v1` is equal to `v2`.
"""

def entance(v1, v2, max_length):
    v1 = v1.lower()
    v2 = v2.lower()

    v1_parts = v1.split('.')
    v2_parts = v2.split('.')

    while len(v1_parts) < len(v2_parts):
        v1_parts.append('0')
    while len(v2_parts) < len(v1_parts):
        v2_parts.append('0')

    for i in range(len(v1_parts)):
        v1_subparts = v1_parts[i].split('-')
        v2_subparts = v2_parts[i].split('-')

        while len(v1_subparts) < len(v2_subparts):
            v1_subparts.append('0')
        while len(v2_subparts) < len(v1_subparts):
            v2_subparts.append('0')

        for j in range(len(v1_subparts)):
            if int(v1_subparts[j]) > int(v2_subparts[j]):
                return 1
            elif int(v1_subparts[j]) < int(v2_subparts[j]):
                return -1

    if len(v1+v2) <= max_length:
        return 0
    else:
        return -2