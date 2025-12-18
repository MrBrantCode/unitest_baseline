"""
QUESTION:
Write a function called `find_first_non_repeating_vowel` that finds the first non-repeating vowel character in a given string of lowercase letters and returns it. If no such character exists, return None. The function should have a time complexity of O(n), where n is the length of the string.
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