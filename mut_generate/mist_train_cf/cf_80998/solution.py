"""
QUESTION:
Write a function named `wordPattern` that takes two parameters: `pattern` and `s`, and returns a boolean value. The function should determine if string `s` adheres to the given `pattern`, where a character in `pattern` corresponds to a non-empty word in `s` in a one-to-one manner.

The function should handle the following constraints:
- The length of `pattern` is between 1 and 300, and it only contains lower-case English letters.
- The length of `s` is between 1 and 3000, and it only contains lower-case English letters and spaces.
- There are no leading or trailing spaces in `s`.
- All words in `s` are separated by a single space.
"""

def wordPattern(pattern, s):
    map_char = {}
    map_word = {}

    words = s.split(' ')
    if len(words) != len(pattern):
        return False

    for p, w in zip(pattern, words):
        if p not in map_char:
            if w in map_word:
                return False
            else:
                map_char[p] = w
                map_word[w] = True
        else:
            if map_char[p] != w:
                return False
    return True