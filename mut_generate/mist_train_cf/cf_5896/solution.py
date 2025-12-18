"""
QUESTION:
Write a function `print_vowels_and_consonants` that takes a string as input, prints the vowels in the string along with their frequency in descending order, and prints the total number of consonants in the string. The function should be case-insensitive, ignore non-alphabet characters, and treat multiple spaces as a single space. The function should have a time complexity of O(n), where n is the length of the string. The input string can have a maximum length of 100 characters.
"""

import re

def print_vowels_and_consonants(string):
    def remove_special_characters(string):
        pattern = r'[^a-zA-Z ]'
        return re.sub(pattern, '', string)

    def merge_multiple_spaces(string):
        pattern = r'\s+'
        return re.sub(pattern, ' ', string)

    def count_consonants(string):
        vowels = 'aeiou'
        consonants = 0
        for char in string.lower():
            if char.isalpha() and char not in vowels:
                consonants += 1
        return consonants

    def count_vowels(string):
        vowels = 'aeiou'
        vowel_counts = {vowel: 0 for vowel in vowels}
        for char in string.lower():
            if char in vowels:
                vowel_counts[char] += 1
        return vowel_counts

    def display_vowel_counts(vowel_counts):
        sorted_counts = sorted(vowel_counts.items(), key=lambda x: x[1], reverse=True)
        for vowel, count in sorted_counts:
            print(f'{vowel}: {count}')

    string = remove_special_characters(string)
    string = merge_multiple_spaces(string)
    consonants = count_consonants(string)
    vowel_counts = count_vowels(string)
    
    print("Vowels:")
    display_vowel_counts(vowel_counts)
    
    print(f"\nTotal number of consonants: {consonants}")