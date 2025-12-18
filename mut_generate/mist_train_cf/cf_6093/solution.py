"""
QUESTION:
Write a function `reverse_words(sentence)` that takes a string sentence as input and returns a string where each word containing at least one vowel is reversed, while other words remain unchanged. The function should be case-insensitive and not use any built-in string manipulation functions or methods. The time complexity should be O(n), where n is the length of the input sentence.
"""

def entance(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = []
    word = ""
    result = []
    
    for char in sentence:
        if char == " ":
            has_vowel = False
            reversed_word = ""
            
            for c in word:
                if c.lower() in vowels:
                    has_vowel = True
                reversed_word = c + reversed_word
            
            if has_vowel:
                result.append(reversed_word)
            else:
                result.append(word)
            
            word = ""
        else:
            word += char
    
    has_vowel = False
    reversed_word = ""
    
    for char in word:
        if char.lower() in vowels:
            has_vowel = True
        reversed_word = char + reversed_word
    
    if has_vowel:
        result.append(reversed_word)
    else:
        result.append(word)
    
    return ' '.join(result)