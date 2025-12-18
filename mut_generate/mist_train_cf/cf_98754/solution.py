"""
QUESTION:
Develop a function called `find_strings` that takes a list of strings as input. Return a list of strings that contain two or more words, start with a vowel, have a length of at least five characters, and do not contain digits or special characters.
"""

def find_strings(input_list):
    output_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for string in input_list:
        if string.count(' ') < 1:
            continue
        if string[0].lower() not in vowels:
            continue
        if any(char.isdigit() or not char.isalnum() for char in string):
            continue
        if len(string) < 5:
            continue
        output_list.append(string)
    return output_list