"""
QUESTION:
Write a function `filter_strings` that takes a list of strings as input and returns a new list containing only the strings that start with a vowel, have a length of at least 5, and contain at least two consecutive vowels, while excluding any strings that contain the word "elephant". The function should be case-insensitive.
"""

def filter_strings(string_list):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for string in string_list:
        if string.lower().startswith(tuple(vowels)) and len(string) >= 5 and 'elephant' not in string.lower():
            consecutive_vowels = False
            for i in range(len(string)-1):
                if string[i].lower() in vowels and string[i+1].lower() in vowels:
                    consecutive_vowels = True
                    break
            if consecutive_vowels:
                result.append(string)
    
    return result