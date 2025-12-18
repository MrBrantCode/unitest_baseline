"""
QUESTION:
Write a function `compress_string` that takes a string as input and returns a compressed string. The compressed string should replace sequences of the same character with the character followed by the count of consecutive occurrences.
"""

def compress_string(s):
    compressed_string = ""
    i = 0

    while i < len(s):
        count = 1
        j = i + 1

        while j < len(s) and s[j] == s[i]:
            count += 1
            j += 1

        compressed_string += s[i] + str(count)
        i = j

    return compressed_string