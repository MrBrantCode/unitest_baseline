"""
QUESTION:
Implement the `consonants_count(s)` function, which takes a string `s` as an argument and returns the total number of consonants present in the string. Consonants include all alphabets except 'a', 'e', 'i', 'o', 'u', and 'y' ONLY when it appears at the end of the provided word. The function should disregard the letter casing and consider special characters within the word.
"""

def consonants_count(s):
    count = 0
    vowels = 'aeiou'
    for char in s.lower():
        if char.isalpha() and char not in vowels and (char != 'y' or char != s[-1].lower()):
            count += 1
    return count