"""
QUESTION:
Write a function `find_first_non_repeating_vowel` that finds the first non-repeating vowel character in a given string of lowercase letters. The function must have a time complexity of O(n) and use constant space. It should not use any additional data structures or built-in string manipulation functions. The string will contain at least one vowel character. If no non-repeating vowel character is found, return an error message.
"""

def find_first_non_repeating_vowel(string):
    vowels = "aeiou"
    vowel_count = [0] * 5
    
    for char in string:
        if char in vowels:
            vowel_count[vowels.index(char)] += 1
    
    for char in string:
        if char in vowels and vowel_count[vowels.index(char)] == 1:
            return char
    
    return "No non-repeating vowel found"