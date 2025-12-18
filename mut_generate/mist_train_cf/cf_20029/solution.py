"""
QUESTION:
Create a function named `rearrange_string` that takes an input string containing only alphabetic characters and spaces. The function should return a string where each word in the input string has its characters reversed, while maintaining the original order of words and handling both uppercase and lowercase letters properly, without using built-in string manipulation functions or libraries.
"""

def rearrange_string(input_string):
    words = input_string.split()
    rearranged_words = []
    for word in words:
        characters = list(word)
        reversed_characters = []
        for i in range(len(characters)-1, -1, -1):
            reversed_characters.append(characters[i])
        reversed_word = ''.join(reversed_characters)
        rearranged_words.append(reversed_word)
    rearranged_string = ' '.join(rearranged_words)
    return rearranged_string