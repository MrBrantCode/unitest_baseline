"""
QUESTION:
Write a function `reverse_vowels` that takes a string as input and returns the string with the vowels in reversed order, while maintaining their original case. The function should work with strings containing both uppercase and lowercase characters.
"""

def reverse_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = [char for char in s if char.lower() in vowels]
    vowel_list.reverse()
    
    modified_string = ""
    vowel_index = 0
    
    for char in s:
        if char.lower() in vowels:
            modified_string += vowel_list[vowel_index]
            vowel_index += 1
        else:
            modified_string += char
    
    return modified_string