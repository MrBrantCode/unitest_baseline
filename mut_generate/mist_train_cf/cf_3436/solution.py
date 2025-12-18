"""
QUESTION:
Find all character positions in a given string, excluding the first and last occurrences of each uppercase letter. The function should return a dictionary where the uppercase letters are keys and their positions are values.
"""

def entrance(s):
    positions = {}
    for i, char in enumerate(s):
        if char.isupper():
            if char in positions:
                if len(positions[char]) == 1:
                    positions[char].append(i)
                elif i not in (positions[char][0], positions[char][-1]):
                    positions[char].append(i)
            else:
                positions[char] = [i]
    return positions