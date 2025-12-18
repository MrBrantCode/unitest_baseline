"""
QUESTION:
Create a function named "convert_sentence" that takes a string as input, checks for numbers, and returns the converted sentence. The function must replace "love" with "like", remove exclamation marks, handle different capitalization, ignore leading and trailing whitespace, and capitalize the first letter of the sentence. If the input sentence contains numbers, the function should raise an exception with the message "Numbers are not allowed in the sentence".
"""

def convert_sentence(sentence):
    if any(char.isdigit() for char in sentence):
        raise Exception("Numbers are not allowed in the sentence")

    sentence = sentence.strip().lower()
    sentence = sentence.replace("love", "like")
    sentence = sentence.replace("!", "")
    return sentence.capitalize()