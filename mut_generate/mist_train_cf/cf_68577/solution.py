"""
QUESTION:
Write a function `compress_string` that compresses a given string by counting the characters and appending the character frequency after each character. The function should also be able to compress the string recursively by introducing a nesting level, denoted with square brackets. A nesting level indicates that the enclosed characters should be compressed further. The function should take two parameters: `string` (the input string to be compressed) and `level` (the nesting level).
"""

def compress_string(string, level):
    compressed = ""
    i = 0

    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            i += 1
            count += 1
        compressed += string[i] + str(count)
        i += 1

    if level == 1:
        return compressed
    else:
        nested_compressed = compress_string(compressed, level - 1)
        if nested_compressed == compressed:
            return compressed
        else:
            return nested_compressed