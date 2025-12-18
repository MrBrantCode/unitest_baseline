"""
QUESTION:
Write a function `find_divisions(s)` that calculates the quantity of beneficial divisions of a string `s` into two non-empty substrings `p` and `q` such that their concatenation equals `s`, the quantity of unique characters in `p` and `q` are identical, the characters in `p` and `q` do not overlap, and the order of characters in `q` is the reverse of the order of characters in `p`. The string `s` only contains lowercase English alphabets and its length is between 1 and 10^6.
"""

def find_divisions(s):
    left_pointer = 0
    right_pointer = len(s) - 1
    left_characters = [0]*26
    right_characters = [0]*26
    left_character_count = 0
    right_character_count = 0
    count = 0

    while right_pointer > left_pointer:
        if left_characters[ord(s[left_pointer]) - ord('a')] == 0:
            left_character_count += 1
        left_characters[ord(s[left_pointer]) - ord('a')] += 1
        left_pointer += 1

        while right_pointer > left_pointer and \
                right_characters[ord(s[right_pointer]) - ord('a')] > 0:
            right_characters[ord(s[right_pointer]) - ord('a')] -= 1
            right_pointer -= 1

        if right_characters[ord(s[right_pointer]) - ord('a')] == 0:
            right_character_count += 1
        right_characters[ord(s[right_pointer]) - ord('a')] += 1

        if left_character_count == right_character_count and \
                left_characters == right_characters:
            count += 1

    return count