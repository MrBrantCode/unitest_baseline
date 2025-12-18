"""
QUESTION:
Construct two Python functions, `how_many_times` and `count_subsequences`, to calculate the frequency of a specified substring within the original string. The `how_many_times` function should consider overlapping instances, while the `count_subsequences` function should consider non-overlapping subsequences. Both functions should take two parameters, `string` and `substring`, and return the frequency of the substring in the string.
"""

def how_many_times(string: str, substring: str) -> int:
    start = 0
    count = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count

def count_subsequences(string: str, substring: str) -> int:
    return string.count(substring)