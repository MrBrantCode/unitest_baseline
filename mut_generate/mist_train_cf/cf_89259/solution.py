"""
QUESTION:
Write a function named `reverse_words` that takes a sentence as input and returns the sentence with each word reversed if it contains at least one vowel. The function should be case-insensitive, meaning it should consider both lowercase and uppercase vowels. The function should not use any built-in string manipulation functions or methods and should have a time complexity of O(n), where n is the length of the input sentence.
"""

def reverse_words(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = sentence.split()
    result = []
    
    for word in words:
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