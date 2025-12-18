"""
QUESTION:
Write a function `find_longest_substring(s)` that finds the length of the longest substring without repeating characters in a given string `s` that contains at least one uppercase letter and one digit. The function should return the length of such a substring. Note that the substring can contain lowercase letters in addition to uppercase letters and digits.
"""

def find_longest_substring(s):
    start = 0
    end = 0
    seen = set()
    result = 0
    has_upper = False
    has_digit = False

    while end < len(s):
        if s[end].isupper():
            has_upper = True
        if s[end].isdigit():
            has_digit = True

        seen.add(s[end])

        if has_upper and has_digit:
            result = max(result, end - start + 1)

        while len(seen) != len(set(s[start:end+1])):
            seen.remove(s[start])
            start += 1

        end += 1

    return result