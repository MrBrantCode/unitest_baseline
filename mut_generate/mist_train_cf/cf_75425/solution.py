"""
QUESTION:
Create a function named `vowel_frequency` that takes a string `s` as input and returns a dictionary with vowel letters as keys and their frequency in the string as values. The function should be case-insensitive and consider both English vowels (a, e, i, o, u) and special accented vowels (é, ü, î, å, ø).
"""

def vowel_frequency(s):
    vowels = 'aeiouéüîåø'
    freq = {vowel: 0 for vowel in vowels}
    
    for char in s.lower():
        if char in vowels:
            freq[char] += 1
            
    return {key: value for key, value in freq.items() if value != 0}