"""
QUESTION:
Write a function `find_longest_substring` that takes a string as input and returns the longest substring without repeating characters and with at least one uppercase letter, one lowercase letter, one digit, and one special character, where each character must be followed by a character that is not the same type (uppercase, lowercase, digit, special character). The function should return an empty string if no such substring exists.
"""

def find_longest_substring(s):
    def is_uppercase(c):
        return 'A' <= c <= 'Z'

    def is_lowercase(c):
        return 'a' <= c <= 'z'

    def is_digit(c):
        return '0' <= c <= '9'

    def is_special(c):
        return not is_uppercase(c) and not is_lowercase(c) and not is_digit(c)

    max_length = 0
    max_substring = ""
    start = 0
    char_types = set()
    char_count = {}

    for end, char in enumerate(s):
        char_types.add((is_uppercase(char), is_lowercase(char), is_digit(char), is_special(char)))
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_types) > 1 and (char_count[char] > 1 or 
            (is_uppercase(char) and is_uppercase(s[end - 1])) or
            (is_lowercase(char) and is_lowercase(s[end - 1])) or
            (is_digit(char) and is_digit(s[end - 1])) or
            (is_special(char) and is_special(s[end - 1]))):
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                char_types.remove((is_uppercase(s[start]), is_lowercase(s[start]), is_digit(s[start]), is_special(s[start])))
            start += 1

        if (any(t) for t in char_types) and len(char_types) == 4 and end - start + 1 > max_length:
            max_length = end - start + 1
            max_substring = s[start:end + 1]

    return max_substring