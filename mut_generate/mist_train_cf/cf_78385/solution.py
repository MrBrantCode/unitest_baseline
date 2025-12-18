"""
QUESTION:
Implement a function named `vowel_swap` that takes a string `text` as input and swaps all instances of every vowel with the subsequent vowel in the English alphabet, considering 'u' as a special case that should be replaced by 'a'. The function should handle both lowercase and uppercase vowels.
"""

def vowel_swap(text):
    vowels = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a', 
              'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
    return ''.join(vowels[ch] if ch in vowels else ch for ch in text)