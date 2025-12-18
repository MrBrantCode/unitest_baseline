"""
QUESTION:
Write a function `compare_versions(version1: str, version2: str) -> int` that compares two version strings following the Semantic Versioning (SemVer) format. The function should return:
- 1 if `version1` is greater than `version2`
- -1 if `version1` is less than `version2`
- 0 if `version1` is equal to `version2`
 
The comparison should prioritize the major, minor, and patch versions, and then the pre-release tags. The pre-release tags should be compared using the following precedence: numeric identifiers are compared numerically, and non-numeric identifiers are compared lexically.
"""

import re

def compare_versions(version1: str, version2: str) -> int:
    def parse_version(version: str) -> tuple:
        version_parts = version.split('+')[0].split('-')[0].split('.')
        pre_release = re.search(r'[-+](.*)', version)
        pre_release_tag = pre_release.group(1) if pre_release else ''
        return tuple(map(int, version_parts)), pre_release_tag

    def compare_pre_release(pre_release1: str, pre_release2: str) -> int:
        if pre_release1 and not pre_release2:
            return -1
        elif not pre_release1 and pre_release2:
            return 1
        elif pre_release1 and pre_release2:
            pre_release1_parts = re.findall(r'[\dA-Za-z-]+', pre_release1)
            pre_release2_parts = re.findall(r'[\dA-Za-z-]+', pre_release2)
            for part1, part2 in zip(pre_release1_parts, pre_release2_parts):
                if part1.isdigit() and part2.isdigit():
                    if int(part1) > int(part2):
                        return 1
                    elif int(part1) < int(part2):
                        return -1
                else:
                    if part1 > part2:
                        return 1
                    elif part1 < part2:
                        return -1
            if len(pre_release1_parts) > len(pre_release2_parts):
                return 1
            elif len(pre_release1_parts) < len(pre_release2_parts):
                return -1
        return 0

    version1_parts, pre_release1 = parse_version(version1)
    version2_parts, pre_release2 = parse_version(version2)

    for v1, v2 in zip(version1_parts, version2_parts):
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1

    if len(version1_parts) > len(version2_parts):
        return 1
    elif len(version1_parts) < len(version2_parts):
        return -1

    return compare_pre_release(pre_release1, pre_release2)