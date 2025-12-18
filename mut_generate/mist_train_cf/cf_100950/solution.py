"""
QUESTION:
Implement a Python function "vowel_trio" that takes a list of strings as input and returns a new list containing only the strings that start with the third vowel after 'y' in the English alphabet. The function should only consider lowercase vowels as valid candidates and should correctly filter the input strings.
"""

def vowel_trio(strings):
    vowels = ["a", "e", "i", "o", "u"]
    new_strings = []
    for string in strings:
        if string[0].lower() == 'y':
            count = 0
            for letter in string[1:]:
                if letter.lower() in vowels:
                    count += 1
                    if count == 3 and letter.lower() == 'i':
                        new_strings.append(string)
                        break
    return new_strings