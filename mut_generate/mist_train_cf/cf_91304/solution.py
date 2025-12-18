"""
QUESTION:
Implement a function `compress_string` that takes a string as input and returns a compressed string. The compressed string should include each character from the original string that occurs more than once, followed by its count. The characters in the compressed string should maintain the order of their first appearance in the original string. The function should return an empty string if no characters occur more than once.
"""

def compress_string(string):
    counts = {}
    compressed = ""

    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for char, count in counts.items():
        if count > 1:
            compressed += char + str(count)

    return compressed