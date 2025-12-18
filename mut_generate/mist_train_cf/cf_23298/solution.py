"""
QUESTION:
Write a function called `toCamelCase` that takes a sentence as input and returns the sentence in camelCase format. The first word should be in lowercase and the first letter of each subsequent word should be uppercase.
"""

def toCamelCase(sentence):
    words = sentence.split(" ")
    result = words[0].lower()
    for word in words[1:]:
        result += word.capitalize()
    return result