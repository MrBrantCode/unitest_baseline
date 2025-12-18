"""
QUESTION:
Create a function `find_string_with_most_vowels` that takes a list of strings as input. The function should return the string with the highest number of vowels, excluding strings that contain numbers and strings with a length of less than 5 characters. If multiple strings have the same highest number of vowels, return the first one that appears in the input list.
"""

def find_string_with_most_vowels(str_list):
    vowels = set("aeiouAEIOU")
    max_vowels = 0
    max_vowel_str = ""
    
    for string in str_list:
        if any(char.isdigit() for char in string):  # skip strings with numbers
            continue
        
        if len(string) < 5:  # skip strings with length < 5
            continue
        
        vowel_count = sum(char in vowels for char in string)
        if vowel_count > max_vowels:
            max_vowels = vowel_count
            max_vowel_str = string
            
    return max_vowel_str