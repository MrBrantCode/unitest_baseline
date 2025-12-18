"""
QUESTION:
Implement a function `longest_vowel_substring(text)` that finds the length of the longest substring of a string `text` that contains only vowels and starts and ends with a consonant. The function should return the length of this substring. The function is case-insensitive and considers 'a', 'e', 'i', 'o', 'u' as vowels.
"""

def longest_vowel_substring(text):
    vowels = set('aeiou')
    max_length = 0
    current_length = 0
    start_index = -1
    
    for i, ch in enumerate(text):
        if ch.lower() in vowels:
            current_length += 1
        else:
            if start_index != -1:
                max_length = max(max_length, current_length)
            current_length = 0
            start_index = -1 if ch.lower() in vowels else i
    
    max_length = max(max_length, current_length)
    return max_length