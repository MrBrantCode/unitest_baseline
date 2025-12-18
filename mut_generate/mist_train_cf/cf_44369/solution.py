"""
QUESTION:
Write a function named `string_reverse` that takes a string `input_string` as input and returns a string where each word is reversed, without using any pre-existing reverse string functionalities or related methods. The input string contains only spaces as delimiters between words.
"""

def string_reverse(input_string):
    words = input_string.split(' ')
    new_words = [word[::-1] for word in words]
    output_string = ' '.join(new_words)
    return output_string