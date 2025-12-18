"""
QUESTION:
Create a function named `find_first_non_repeating_vowel(s)` that takes a string `s` as input, which only contains lowercase letters, and returns the first non-repeating vowel character in the string. If no non-repeating vowel character is found, return `None`.
"""

def find_first_non_repeating_vowel(s):
    vowel_count = {}
    vowels = []

    for ch in s:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            if ch not in vowel_count:
                vowel_count[ch] = 1
            else:
                vowel_count[ch] += 1
            if ch not in vowels:
                vowels.append(ch)

    for v in vowels:
        if vowel_count[v] == 1:
            return v

    return None