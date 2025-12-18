"""
QUESTION:
Write a function `find_string_with_most_vowels` that takes a list of strings as input. The function must exclude any strings containing numbers and those that are less than 5 characters in length, and return the string with the highest number of vowels. If there are multiple strings with the same number of vowels, return the first one that appears in the input list.
"""

def find_string_with_most_vowels(str_list):
    vowels = set("aeiouAEIOU")
    max_vowels = 0
    max_vowel_str = ""

    for string in str_list:
        if any(char.isdigit() for char in string):  
            continue
        
        if len(string) < 5:  
            continue
        
        vowel_count = sum(char in vowels for char in string)
        if vowel_count > max_vowels:
            max_vowels = vowel_count
            max_vowel_str = string
            
    return max_vowel_str