"""
QUESTION:
Write a function `compress(chars)` that takes an array of characters `chars` as input, compresses it in-place, and returns the new length of the array. The compression is done by replacing each group of consecutive repeating characters with the character followed by the group's length. If the group's length is 1, only the character is appended. If the group's length is 10 or longer, it is split into multiple characters in `chars`, with each character representing a digit of the group's length. The function should use O(1) extra space.
"""

def compress(chars):
    write = anchor = 0
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    return write