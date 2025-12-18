"""
QUESTION:
Implement a function named `is_happy_complex` that determines if a given string `s` meets the following conditions:
- The string's length is at least three characters.
- Each successive triplet of characters has unique characters.
- Each unique character appears at least twice in the entire string.
- There is no repetition of the same letter immediately.
- There is at least one character that is next to its succeeding character in the English alphabet.
Use a dictionary to keep track of each character's appearances in the string.
"""

def is_happy_complex(s):
    if len(s) < 3: return False
    
    character_appearances = {}
    prev_char = s[0]
    for char in s[1:]:
        if char in character_appearances:
            character_appearances[char] += 1
        else:
            character_appearances[char] = 1
        if prev_char == char: return False
        prev_char = char

    if any(value < 2 for value in character_appearances.values()): return False

    triplets = [s[i:i+3] for i in range(len(s)-2)]
    for triplet in triplets:
        if len(set(triplet)) != len(triplet): return False
    
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i+1])) == 1: break
    else: return False

    return True