"""
QUESTION:
Write a function called `is_palindrome` that takes a single string argument `sentence` containing at least one word and no more than 100 characters. The function should remove all spaces and punctuation marks from the sentence, convert it to lowercase, and then return True if the resulting string is the same when its characters are reversed and False otherwise.
"""

def entance(sentence):
    sentence = sentence.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace("\"", "").replace(":", "").replace(";", "")
    sentence = sentence.lower()
    return sentence == sentence[::-1]