"""
QUESTION:
Write a function `are_anagrams(string1, string2)` that checks if two given strings are anagrams of each other and contain at least one vowel and one consonant. The function should return True if the strings meet the conditions and False otherwise. The function should ignore case sensitivity and consider empty strings as invalid input.
"""

def are_anagrams(string1, string2):
    if string1 == '' or string2 == '':
        return False
    
    string1 = string1.lower()
    string2 = string2.lower()
    
    string1_dict = {}
    string2_dict = {}
    
    for char in string1:
        string1_dict[char] = string1_dict.get(char, 0) + 1
    
    for char in string2:
        string2_dict[char] = string2_dict.get(char, 0) + 1
    
    if not string1_dict or not string2_dict:
        return False
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(c) for c in range(ord('a'), ord('z')+1) if chr(c) not in vowels]
    
    vowel_found = False
    consonant_found = False
    
    for char in string1_dict:
        if char in vowels:
            vowel_found = True
        if char in consonants:
            consonant_found = True
    
    for char in string2_dict:
        if char in vowels:
            vowel_found = True
        if char in consonants:
            consonant_found = True
    
    if not vowel_found or not consonant_found:
        return False
    
    return string1_dict == string2_dict