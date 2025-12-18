"""
QUESTION:
Create a function `analyze_string(s)` that takes a string `s` as input and returns a dictionary with three values: the index of the first unique character in the string, the frequency distribution of all characters in the string, and the frequency of each vowel in the string. The frequency distribution should be a list of tuples, where each tuple contains a character and its frequency, sorted in ascending order by character. The vowel frequency should be a dictionary with the frequency of each vowel, also sorted in ascending order by character. All characters should be treated as lowercase for the purpose of frequency distribution count.
"""

from collections import Counter

def analyze_string(s):
    s_lower = s.lower()
    freq_dist = sorted(Counter(s_lower).items())
    first_unique_char_index = None

    for char, freq in freq_dist:
        if freq == 1:
            first_unique_char_index = s.index(char)
            break

    vowel_freq = dict.fromkeys('aeiou', 0)
    for char, freq in freq_dist:
        if char in vowel_freq:
            vowel_freq[char] = freq

    return {
        'first_unique_char_index': first_unique_char_index,
        'frequency_dist': freq_dist,
        'vowel_freq': dict(sorted(vowel_freq.items()))
    }