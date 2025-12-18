"""
QUESTION:
Create a function `capitalize_sentence` that takes a sentence as input and returns the sentence with each word capitalized, without using built-in string functions or methods that directly capitalize words or convert strings to title case. The input sentence can contain multiple words separated by spaces.
"""

def capitalize_sentence(sentence):
    result = ''
    capitalize_next = True

    for char in sentence:
        if char == ' ':
            result += char
            capitalize_next = True
        else:
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char.lower()

    return result