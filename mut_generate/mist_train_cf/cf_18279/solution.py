"""
QUESTION:
Create a function named `count_characters` that takes a string as input and returns a list containing the number of alphabetic characters in each word of the string. Words are defined as sequences of alphabetic characters, and punctuation marks and special characters are considered separate words and should not be included in the character count. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in functions or libraries for splitting the string into words.
"""

def count_characters(sentence):
    word_lengths = []
    current_length = 0

    for char in sentence:
        if char.isalpha():
            current_length += 1
        elif current_length > 0:
            word_lengths.append(current_length)
            current_length = 0

    if current_length > 0:
        word_lengths.append(current_length)

    return word_lengths