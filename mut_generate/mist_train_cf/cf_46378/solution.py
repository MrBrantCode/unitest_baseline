"""
QUESTION:
Develop a function `first_non_repeating` that takes a string of alphabetic characters as input and returns the positional index of the earliest character that doesn't recur elsewhere within the string. Assume the input string only contains alphabetic characters, no special symbols, and may contain both lowercase and uppercase letters. If no such character exists, return -1. The solution should not use built-in Python functions except for determining string length.
"""

def firstNonRepeatingCharacter(s):
    repeats = [0 for _ in range(52)]
    index = [0 for _ in range(52)]

    for i in range(len(s)):
        char = s[i]
        if char.islower():
            char_index = ord(char) - ord('a')
        else:
            char_index = ord(char) - ord('A') + 26
        if repeats[char_index] == 0:
            repeats[char_index] += 1
            index[char_index] = i
        else:
            repeats[char_index] += 1

    min_index = float('inf')
    for i in range(52):
        if repeats[i] == 1:
            min_index = min(min_index, index[i])

    return min_index if min_index != float('inf') else -1