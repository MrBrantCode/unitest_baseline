"""
QUESTION:
Implement a function `modify_string(original, target)` that determines if a given character sequence (`original`) can be modified to exactly match another sequence (`target`) by performing a single character insertion, removal, or replacement, and ensuring the result matches the regex protocol `/^[a-z]+$/`. The function should return `True` if a match is possible and `False` otherwise. The function should be able to handle strings of up to 10^6 characters in length. The sequences should only include lowercase letters.
"""

import re

def modify_string(original, target):
    original_len = len(original)
    target_len = len(target)

    # check for insert
    if original_len+1 == target_len:
        for i in range(target_len):
            if i == target_len-1 or original[i] != target[i]:
                # if we reach the end of original or find different char, we insert the target char
                new_string = original[:i] + target[i] + original[i:]
                if re.fullmatch('^[a-z]+$', new_string) and new_string == target:
                    return True

    # check for remove
    elif original_len-1 == target_len:
        for i in range(original_len):
            if i == original_len-1 or original[i] != target[i]:
                # if we reach the end of original or find different char, we remove the original char
                new_string = original[:i] + original[i+1:]
                if re.fullmatch('^[a-z]+$', new_string) and new_string == target:
                    return True

    # check for replace
    elif original_len == target_len:
        for i in range(original_len):
            if original[i] != target[i]:
                # if we find different char, we replace the original char
                new_string = original[:i] + target[i] + original[i+1:]
                if re.fullmatch('^[a-z]+$', new_string) and new_string == target:
                    return True

    # if none of the modifications work, return False
    return False