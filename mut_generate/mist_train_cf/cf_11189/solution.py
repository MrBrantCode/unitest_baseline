"""
QUESTION:
Create a function called `convert_string` that takes a string as input. The function should convert the string to lower case and remove any special characters, numbers, and whitespace. It should then count the occurrences of each letter in the string and return a dictionary with the letter as the key and its count as the value.
"""

def convert_string(string):
    string = string.lower()
    string = ''.join(e for e in string if e.isalpha())
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count