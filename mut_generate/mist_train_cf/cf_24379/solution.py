"""
QUESTION:
Given a string, write a function `find_character_positions` that returns a dictionary where the keys are unique characters in the string and the values are lists of their corresponding positions in the string. The positions are 0-indexed, meaning the first character is at position 0.
"""

def find_character_positions(s):
    positions = {}
    for i, char in enumerate(s):
        if char in positions:
            positions[char].append(i)
        else:
            positions[char] = [i]
    return positions