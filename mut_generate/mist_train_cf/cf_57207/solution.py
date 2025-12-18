"""
QUESTION:
Create a function `character_frequency(s)` that takes a string `s` as input and returns the frequency of each alphabet character, along with the characters that appear most frequently and least frequently. The function should ignore non-alphabet characters and treat uppercase and lowercase letters as the same. It should also handle the case where the string is empty. If there is a tie for either the most or least frequent characters, return all characters that are tied.
"""

def character_frequency(s):
    if not s:
        return "The string is empty."

    freq_map = {}
    s = s.lower()

    for char in s:
        if char.isalpha():
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1

    min_freq = min(freq_map.values())
    max_freq = max(freq_map.values())
    min_freq_chars = [k for k, v in freq_map.items() if v == min_freq]
    max_freq_chars = [k for k, v in freq_map.items() if v == max_freq]

    return "The frequencies of characters are: {}\nMost frequent character(s): {}\nLeast frequent character(s): {}".format(freq_map, max_freq_chars, min_freq_chars)