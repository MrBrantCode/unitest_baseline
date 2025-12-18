"""
QUESTION:
Create a function called `get_first_letters` that takes a string as input and returns the first letter of each word in uppercase, excluding vowels and any non-alphabetic characters. The function should have a time complexity of O(n), where n is the length of the string. The input string may contain alphabetic characters, spaces, special characters, and numbers.
"""

def get_first_letters(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""

    words = input_string.split()

    for word in words:
        if len(word) == 0 or word[0].lower() in vowels or not word[0].isalpha():
            continue

        result += word[0].upper()

    return result