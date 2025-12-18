"""
QUESTION:
Write a function called `capitalize_sentence` that takes a string `sentence` as input and returns a new string where the first letter of each word in the sentence is capitalized and the rest of the letters are in lowercase. The function should handle sentences with multiple words separated by spaces.
"""

def capitalize_sentence(sentence):
    words = sentence.split(' ')
    capitalized_words = [word.capitalize() for word in words]
    capitalized_sentence = ' '.join(capitalized_words)
    return capitalized_sentence