"""
QUESTION:
Create a function named `get_first_letters` that takes a string as input. The function should return the first letter of each word in the string, excluding any words that start with a vowel (a, e, i, o, u). The returned letters should be in uppercase. The function should ignore any non-alphabetic characters and have a time complexity of O(n), where n is the length of the string.
"""

def get_first_letters(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""

    words = input_string.split()

    for word in words:
        if len(word) == 0 or word[0].lower() in vowels:
            continue

        result += word[0].upper()

    return result