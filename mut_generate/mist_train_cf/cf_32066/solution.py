"""
QUESTION:
Write a function `countDistinctCharacters` that takes a string of lowercase English letters as input and returns the count of each distinct character in the format "character count". The output should be in the order the characters first appear in the string.
"""

def countDistinctCharacters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    result = []
    for char, count in char_count.items():
        result.append(f"{char} {count}")
    
    return result