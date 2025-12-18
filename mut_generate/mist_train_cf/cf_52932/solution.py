"""
QUESTION:
Create a function named `swap_vowels` that takes a string as input. The function should swap all instances of vowels in the string with the next vowel in the series ('a' with 'e', 'e' with 'i', 'i' with 'o', 'o' with 'u', and 'u' with 'a') in a circular manner and return the resulting string.
"""

def swap_vowels(text):
    vowels = 'aeiou'
    swapped_text = ''
    
    for char in text:
        if char in vowels:
            index = vowels.index(char)
            # add 1 to the index and use modulo to make the series circular
            swapped_text += vowels[(index + 1) % len(vowels)]
        else:
            swapped_text += char
    
    return swapped_text