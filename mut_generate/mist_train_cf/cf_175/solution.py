"""
QUESTION:
Write a function called `find_first_non_repeating_character` that takes a string as input and returns the first non-repeating character in the string. The function should handle both uppercase and lowercase letters as separate characters, as well as special characters and numbers. If no non-repeating character is found, the function should return the string "No non-repeating character found". The function must have a time complexity of O(n), where n is the length of the input string.
"""

def find_first_non_repeating_character(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    for char in string:
        if char_count[char] == 1:
            return char

    return "No non-repeating character found"