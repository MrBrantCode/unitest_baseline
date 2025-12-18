"""
QUESTION:
Write a function `most_frequent_letter(s)` that takes a string `s` as input and returns the most frequent letter in the string. If there are multiple letters with the same highest frequency, return the letter that appears first in the string. If the string is empty, return an empty string.
"""

def most_frequent_letter(s):
    if not s:
        return ""
    
    freq_dict = {}
    for char in s:
        if char.isalpha():
            char = char.lower()
            freq_dict[char] = freq_dict.get(char, 0) + 1
    
    max_freq = max(freq_dict.values())
    most_freq_letter = next(char for char, freq in freq_dict.items() if freq == max_freq)
    
    return most_freq_letter