"""
QUESTION:
Implement a function `count_true` that counts the number of occurrences of a given substring within a string. The function should be case-insensitive and consider overlapping occurrences of the substring. 

The function `count_true` takes two parameters: `string` and `substring`. The length of `string` is between 1 and 10^5, and the length of `substring` is between 1 and 10. The function returns an integer representing the total number of occurrences of the substring within the given string.
"""

def count_true(string: str, substring: str) -> int:
    count = 0
    string = string.lower()
    substring = substring.lower()
    start = 0
    while start < len(string):
        index = string.find(substring, start)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break
    return count