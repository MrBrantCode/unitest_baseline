"""
QUESTION:
Find the longest word in a dictionary that can be constructed from a given set of characters, with the following restrictions:
- The characters in the set can be used multiple times to construct the word.
- The constructed word must contain at least one vowel.
- The solution must handle case-insensitivity of the characters in the set and dictionary.
- The function must have a time complexity of O(n), where n is the length of the dictionary. 

Function name: longest_word_from_characters 
Input parameters: a dictionary of words and a set of characters.
"""

def longest_word_from_characters(dictionary, characters):
    """
    This function finds the longest word in a dictionary that can be constructed from a given set of characters.
    
    Parameters:
    dictionary (list): A list of words
    characters (set): A set of characters
    
    Returns:
    str: The longest word that can be constructed from the given set of characters with at least one vowel
    """
    vowels = set('aeiouAEIOU')
    max_length_word = ""

    for word in dictionary:
        if len(word) > len(max_length_word):
            word_lower = word.lower()
            char_set = set(characters)
            contains_vowel = False
            
            for char in char_set:
                if char in vowels:
                    char_set.remove(char)
                    contains_vowel = True
                    break
            
            if not contains_vowel:
                continue
            
            for char in word_lower:
                if char in char_set:
                    char_set.remove(char)
            
            if len(char_set) < len(set(characters)):
                max_length_word = word

    return max_length_word