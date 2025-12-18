"""
QUESTION:
Given a string of lowercase English words with a maximum length of 1000 characters and a list of distinct consonants, write a function `character_freq_and_absentee` that takes these two inputs and returns two outputs: 
1. A dictionary of unique consonants from the list that are present in the string, along with their occurrence count.
2. A list of consonants from the input list that do not occur in the string.
"""

def character_freq_and_absentee(string, specific_chars):
    freq_dict = {char: 0 for char in specific_chars}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
    absentee_chars = [char for char, freq in freq_dict.items() if freq == 0]
    present_chars = {char: freq for char, freq in freq_dict.items() if freq != 0}
    return present_chars, absentee_chars