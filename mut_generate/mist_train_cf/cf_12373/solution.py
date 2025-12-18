"""
QUESTION:
Write a function `reverse_and_replace_vowels` that takes a string `string` and a list `replacements` as input, reverses the order of `string`, and replaces all vowels in the reversed string with the corresponding vowel from `replacements` where the index of the replacement vowel is determined by the position of the original vowel in the string "aeiou". The replacement should be case-insensitive.
"""

def reverse_and_replace_vowels(string, replacements):
    vowels = "aeiou"
    reversed_string = string[::-1]  # Reverse the order of the string

    # Replace vowels with corresponding replacements
    replaced_string = ""
    for char in reversed_string:
        if char.lower() in vowels:
            vowel_index = vowels.index(char.lower())
            if char.isupper():
                replaced_string += replacements[vowel_index].upper()
            else:
                replaced_string += replacements[vowel_index]
        else:
            replaced_string += char

    return replaced_string