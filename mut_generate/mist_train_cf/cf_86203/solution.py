"""
QUESTION:
Create a function named `count_vowels` that takes a string `text` as input and returns a dictionary where the keys are the vowels 'a', 'e', 'i', 'o', 'u' and the values are the counts of each vowel in the input string. The function should be case-insensitive and should not use any built-in functions or libraries that directly count the number of vowels in the string.
"""

def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_counts = {vowel: 0 for vowel in vowels}
    
    for char in text:
        if char.lower() in vowels:
            vowel_counts[char.lower()] += 1
    
    return vowel_counts