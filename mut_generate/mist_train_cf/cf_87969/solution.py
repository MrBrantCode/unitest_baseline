"""
QUESTION:
Write a function `find_character_positions` that takes a string as input, finds all character positions of uppercase letters, excluding the first and last occurrences of each character, and returns a dictionary with uppercase letters as keys and a list of their positions as values. If there are multiple characters with the same uppercase letter, consider them as separate characters.
"""

def find_character_positions(string):
    positions = {}
    for i, char in enumerate(string):
        if char.isupper():
            if char in positions:
                if i not in positions[char]:
                    positions[char].append(i)
            else:
                positions[char] = [i]
    return positions