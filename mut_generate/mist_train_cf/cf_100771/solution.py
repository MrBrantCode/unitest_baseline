"""
QUESTION:
Create a function `arrange_sentence(words)` that takes a list of words as input and returns a string representing a valid sentence. The function should capitalize the first word and arrange the words in the correct order, separated by spaces, and append a period at the end of the sentence. The input list is assumed to contain at least one word.
"""

def arrange_sentence(words):
    # Convert the first word to title case and add it to the result string
    result = words[0].capitalize()
    # Add the rest of the words to the result string, separated by spaces
    for word in words[1:]:
        result += ' ' + word
    # Add a period at the end of the sentence
    result += '.'
    return result