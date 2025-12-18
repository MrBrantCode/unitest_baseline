"""
QUESTION:
Find the most frequent non-vowel character in a list of strings. The function `find_most_frequent_non_vowel(strings)` should take a list of strings as input and return the most frequent non-vowel character. If there are multiple characters that are equally the most frequent, return the one that appears first in the list. Ignore case sensitivity when checking for vowels and ignore spaces when counting the frequency of characters. If all the characters in the strings are vowels, return None. If all the characters in the strings are non-vowels, return the most frequent character regardless of being a vowel or not. The solution should have a time complexity of O(n), where n is the total number of characters in the list of strings, and a space complexity of O(1).
"""

def find_most_frequent_non_vowel(strings):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    frequencies = {}
    max_frequency = 0
    most_frequent_character = None
    
    for string in strings:
        for char in string:
            char_lower = char.lower()
            
            if char_lower in vowels or char_lower == ' ':
                continue
            
            if char_lower in frequencies:
                frequencies[char_lower] += 1
            else:
                frequencies[char_lower] = 1
            
            if frequencies[char_lower] > max_frequency:
                max_frequency = frequencies[char_lower]
                most_frequent_character = char_lower
                
    if not frequencies:
        return None
    
    return most_frequent_character