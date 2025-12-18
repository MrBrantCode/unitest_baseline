"""
QUESTION:
Write a function named `filter_strings` that takes a list of strings as input and returns a new list containing only the strings that meet the following conditions: 
- The string starts with a vowel (either uppercase or lowercase).
- The string has a length of at least 5 characters.
- The string contains at least two consecutive vowels (either uppercase or lowercase).
"""

def filter_strings(strings):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_strings = []
    
    for string in strings:
        if string[0].lower() in vowels and len(string) >= 5:
            consecutive_vowels = False
            for i in range(len(string)-1):
                if string[i].lower() in vowels and string[i+1].lower() in vowels:
                    consecutive_vowels = True
                    break
            if consecutive_vowels:
                filtered_strings.append(string)
    
    return filtered_strings