"""
QUESTION:
Write a function named `countSubstringOccurrences` that takes two string inputs, `larger_string` and `substring`, and returns the number of occurrences of `substring` within `larger_string` as an integer. The function should be able to handle cases where the `substring` appears multiple times in `larger_string`. The input strings only contain lowercase English letters. The `substring` is not empty and is not longer than `larger_string`.
"""

def countSubstringOccurrences(larger_string: str, substring: str) -> int:
    count = 0
    start = 0
    while start < len(larger_string):
        index = larger_string.find(substring, start)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break
    return count