"""
QUESTION:
Write a function `find_divisions(s)` that takes a string `s` as input and returns the number of divisions in the string where the left and right substrings have the same character count and the same characters. The function should iterate through the string from both ends, keeping track of the character counts and unique characters on both sides. The function should return the total count of such divisions. The input string `s` only contains lowercase English letters.
"""

def find_divisions(s):
    # Initialize variables (pointers and arrays)
    left_pointer = 0
    right_pointer = len(s) - 1
    left_characters = [0]*26
    right_characters = [0]*26
    left_character_count = 0
    right_character_count = 0
    count = 0

    while right_pointer > left_pointer:
        # Iterate through the string from left
        if left_characters[ord(s[left_pointer]) - ord('a')] == 0:
            left_character_count += 1
        left_characters[ord(s[left_pointer]) - ord('a')] += 1
        left_pointer += 1

        # Iterate through the string from right
        while right_pointer > left_pointer and \
        right_characters[ord(s[right_pointer]) - ord('a')] <= 0:
            right_characters[ord(s[right_pointer]) - ord('a')] += 1
            right_pointer -= 1
            
        # Add unique character count to right character count
        if right_characters[ord(s[right_pointer]) - ord('a')] == 0:
            right_character_count += 1
        right_characters[ord(s[right_pointer]) - ord('a')] += 1

        # Compare character counts and update
        if left_character_count == right_character_count and \
        left_characters == right_characters:
            count += 1

    return count