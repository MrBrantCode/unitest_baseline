"""
QUESTION:
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:


Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:


Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:


Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
"""

def compare_versions(version1: str, version2: str) -> int:
    while version1 and version2:
        result1 = version1.split('.', 1)
        if len(result1) == 2:
            (digit1, version1) = (result1[0], result1[1])
        else:
            digit1 = result1[0]
            version1 = ''
        
        result2 = version2.split('.', 1)
        if len(result2) == 2:
            (digit2, version2) = (result2[0], result2[1])
        else:
            digit2 = result2[0]
            version2 = ''
        
        if int(digit1) > int(digit2):
            return 1
        elif int(digit1) < int(digit2):
            return -1
    
    if version1 and sum(map(lambda x: int(x), version1.split('.'))) != 0:
        return 1
    if version2 and sum(map(lambda x: int(x), version2.split('.'))) != 0:
        return -1
    
    return 0