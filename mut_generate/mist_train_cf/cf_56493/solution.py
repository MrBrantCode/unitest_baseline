"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the string with all alphabetic characters reversed, while maintaining the positions of non-alphabetic characters. The function must not use any built-in string reversal methods and should correctly handle Unicode characters.
"""

def reverse_string(input_string):
    input_string = list(input_string)
    i, j = 0, len(input_string) - 1

    while i < j:
        if not input_string[i].isalpha():
            i += 1
        elif not input_string[j].isalpha():
            j -= 1
        else:
            input_string[i], input_string[j] = input_string[j], input_string[i]
            i += 1
            j -= 1

    return ''.join(input_string)