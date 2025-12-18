"""
QUESTION:
Create a function `reverse_vowels` that takes a string as input and returns a new string where every vowel is in reverse order. The vowels should be reversed in the order of their appearance in the string, not alphabetically. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_vowels(string):
    vowels = []
    for char in string:
        if char.lower() in "aeiou":
            vowels.append(char)

    vowels = vowels[::-1]  # Reverse the list of vowels

    new_string = ""
    vowel_index = 0
    for char in string:
        if char.lower() in "aeiou":
            new_string += vowels[vowel_index]
            vowel_index += 1
        else:
            new_string += char

    return new_string