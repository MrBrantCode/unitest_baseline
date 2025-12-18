"""
QUESTION:
Write a function `convert_to_dictionary` that takes a list of strings as input and returns a dictionary whose keys are numbers in ascending order starting from 1 and values are strings in uppercase letters. The function should exclude strings with less than 8 characters, strings with repeated characters, palindromes, and strings with less than 3 vowels.
"""

def convert_to_dictionary(string_list):
    result = {}
    count = 1
    for string in string_list:
        uppercase_string = string.upper()
        if len(uppercase_string) >= 8 and len(set(uppercase_string)) == len(uppercase_string) and uppercase_string[::-1] != uppercase_string:
            vowels_count = 0
            for char in uppercase_string:
                if char in "AEIOU":
                    vowels_count += 1
            if vowels_count >= 3:
                result[count] = uppercase_string
                count += 1
    return result