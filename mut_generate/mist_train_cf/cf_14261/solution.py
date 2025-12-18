"""
QUESTION:
Write a function called `remove_pattern` that takes two strings, `string` and `pattern`, and returns a new string with all occurrences of `pattern` removed. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def remove_pattern(string, pattern):
    result = ""
    i = j = 0

    while i < len(string):
        if string[i:i + len(pattern)] == pattern:
            i += len(pattern)
            j = i
        else:
            result += string[i]
            i += 1
            j += 1

    return result