"""
QUESTION:
Write a function `reverse_position(s)` that takes a string `s` as input and returns a string with the positions of all vowel-consonant pairs reversed, while keeping all other characters in their original positions. Vowels are defined as the characters 'a', 'e', 'i', 'o', and 'u', and the function should be case-insensitive when identifying vowels. The function should preserve the case of the characters while swapping.
"""

def reverse_position(s):
    vowel = 'aeiou'
    string_list = list(s)
    i, j = 0, len(s)-1
    while i<j:
        if (string_list[i].lower() in vowel and string_list[j].lower() not in vowel) or (string_list[i].lower() not in vowel and string_list[j].lower() in vowel):
            string_list[i], string_list[j] = string_list[j], string_list[i]
            i += 1
            j -= 1
        elif string_list[i].lower() not in vowel and string_list[j].lower() not in vowel:
            i += 1
        elif string_list[i].lower() in vowel and string_list[j].lower() in vowel:
            j -= 1
    return ''.join(string_list)