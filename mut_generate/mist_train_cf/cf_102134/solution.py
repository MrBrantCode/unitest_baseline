"""
QUESTION:
Create a function named `reverse_lookup` that takes a list of words as input. The function should return a dictionary where each key is a word from the input list (case insensitive) and its corresponding value is a list of indices where the word appears in the input list, but only include words that contain at least two vowels (case insensitive).
"""

def reverse_lookup(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    reverse_dict = {}
    
    for i, word in enumerate(words):
        lowercase_word = word.lower()
        vowel_count = sum(1 for char in lowercase_word if char in vowels)
        
        if vowel_count >= 2:
            reverse_dict.setdefault(lowercase_word, []).append(i)
                
    return reverse_dict