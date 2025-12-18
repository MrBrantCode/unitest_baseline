"""
QUESTION:
Create a function `count_vowels_positions(s)` that takes a string `s` as input and returns a dictionary with the count and positions of each vowel ('a', 'e', 'i', 'o', 'u') in the string, ignoring case, special characters, and numbers. The function should have a maximum input string length of 1000 characters and handle it in a time and space efficient manner.
"""

def count_vowels_positions(s):
    vowels_positions = {'a': [], 'e': [], 'i': [], 'o': [], 'u': []}
    
    for i in range(len(s)):
        char = s[i].lower()
        if char in vowels_positions:
            vowels_positions[char].append(i+1)
            
    return vowels_positions