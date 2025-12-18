"""
QUESTION:
Implement a function `compress_string` that takes a string as input and returns a compressed string where each character is followed by its count, but only include characters that occur more than once in the original string, maintaining their order of appearance.
"""

def compress_string(s):
    counts = {}
    compressed = ""

    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for char, count in counts.items():
        if count > 1:
            compressed += char + str(count)

    return compressed