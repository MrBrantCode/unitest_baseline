"""
QUESTION:
Implement the function `swap_vowels(text)` that swaps all instances of vowels in the provided text with the next vowel in the sequence ('a' with 'e', 'e' with 'i', 'i' with 'o', 'o' with 'u', and 'u' with 'a'). The solution should be case-sensitive, meaning upper-case vowels are replaced with their upper-case counterparts, not their lower-case counterparts.
"""

def swap_vowels(text):
    vowels = 'aeiouAEIOU'
    next_vowels = 'eiouaEIOUA'
    map_vowels = str.maketrans(vowels, next_vowels)
    return text.translate(map_vowels)