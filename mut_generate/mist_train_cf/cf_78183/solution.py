"""
QUESTION:
Create a function `enhanced_vowels_count` that accepts a string representing a word and returns the total number of vowels present, including all instances of 'a', 'e', 'i', 'o', 'u', and 'y' only when it is the last letter of the word. The function should ignore case and take into account special characters and diacritics.
"""

def enhanced_vowels_count(s):
    """Create a function enhanced_vowels_count that accepts a string representing
    a word and returns the total number of vowels present, including all instances of 'a', 'e', 'i', 'o', 'u',
    and 'y' ONLY when it is the last letter of the word. Ignore case, and take into account special characters and diacritics."""
    
    vowels = "aeiou"
    count = sum(s.lower().count(v) for v in vowels)
    
    if s and s[-1].lower() == 'y':
        count += 1
    
    for c in "áéíóúàèìòùâêîôûãõ":
        count += s.lower().count(c)
    
    return count