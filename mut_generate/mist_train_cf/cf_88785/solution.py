"""
QUESTION:
Create a function named `convert_string` that takes an input string as a parameter. The input string contains only alphabetic characters and whitespace. The function should convert each word in the string to uppercase, replace all vowels (A, E, I, O, U) with their corresponding numbers (A=1, E=2, I=3, O=4, U=5), and return a string with the converted words separated by a single whitespace and no leading or trailing whitespaces.
"""

def convert_string(input_string):
    vowels = {'A': '1', 'E': '2', 'I': '3', 'O': '4', 'U': '5'}
    words = input_string.upper().split()
    converted_words = []
    for word in words:
        converted_word = ''
        for char in word:
            if char in vowels:
                converted_word += vowels[char]
            else:
                converted_word += char
        converted_words.append(converted_word)
    return ' '.join(converted_words)