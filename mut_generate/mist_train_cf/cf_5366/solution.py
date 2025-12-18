"""
QUESTION:
Create a function `alternate_vowels` that takes two strings as input. The function should alternate the vowels from both strings in reverse order of their original appearance, remove any duplicates, and return the resulting string. The vowels are considered in lowercase, regardless of their original case. The function should have a time complexity of O(n), where n is the total number of characters in the input strings.
"""

def alternate_vowels(string1, string2):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels_in_string1 = []
    vowels_in_string2 = []
    
    for char in string1:
        if char.lower() in vowels:
            vowels_in_string1.append(char.lower())
    
    for char in string2:
        if char.lower() in vowels:
            vowels_in_string2.append(char.lower())
    
    vowels_in_string1.reverse()
    vowels_in_string2.reverse()
    
    output = ''
    seen = set()
    
    for vowel in vowels_in_string1:
        if vowel not in seen:
            output += vowel
            seen.add(vowel)
    
    for vowel in vowels_in_string2:
        if vowel not in seen:
            output += vowel
            seen.add(vowel)
    
    return output