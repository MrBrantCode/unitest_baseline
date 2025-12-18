"""
QUESTION:
Write a function named `compress_string` that takes a string as input and returns a string where each sequence of consecutive occurrences of a character is replaced by a tuple in the format `(character, count)`. The function must not use any built-in functions for string manipulation or counting and must not use any additional data structures such as dictionaries or lists.
"""

def compress_string(s):
    if not s:
        return ""

    compressed = ""
    prev_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            compressed += "(" + prev_char + "," + str(count) + ")"
            prev_char = s[i]
            count = 1

    compressed += "(" + prev_char + "," + str(count) + ")"
    return compressed