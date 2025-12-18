"""
QUESTION:
Write a function `find_positions(s, ch)` that takes a string `s` and a character `ch` as inputs, and returns a list of absolute positions of every instance of `ch` in `s` (counting from zero) along with the total frequency of `ch`. Implement this without using any inbuilt search functions, only using basic string manipulations and loop structures.
"""

def find_positions(s, ch):
    positions = []
    frequency = 0
    for i in range(len(s)):
        if s[i] == ch:
            positions.append(i)
            frequency += 1
    return positions, frequency