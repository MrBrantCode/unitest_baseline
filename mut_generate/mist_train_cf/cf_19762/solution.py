"""
QUESTION:
Write a function named `reverse_string_with_vowel_replacements` that takes two parameters: `input_string` and `replacements`. The function should reverse the order of the characters in `input_string` and replace the vowels with the corresponding vowel from the `replacements` list, ignoring non-alphabetic characters. The `replacements` list is assumed to contain five elements corresponding to the vowels 'a', 'e', 'i', 'o', 'u' in order.
"""

def reverse_string_with_vowel_replacements(input_string, replacements):
    vowels = 'aeiou'
    output_string = ''
    
    # Reverse the input string
    input_string = input_string[::-1]
    
    for char in input_string:
        if char.isalpha():
            if char.lower() in vowels:
                # Find the index of the vowel in the vowels string
                vowel_index = vowels.index(char.lower())
                # Replace the vowel with the corresponding vowel from the replacements list
                output_string += replacements[vowel_index]
            else:
                # Add non-vowel alphabetic characters as is
                output_string += char
        else:
            output_string += char
    
    return output_string