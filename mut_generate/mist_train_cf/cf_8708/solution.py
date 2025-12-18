"""
QUESTION:
Implement a function called `replace_hello` that takes a string as input and replaces the word "Hello" with "Goodbye" if it appears at the beginning of a sentence (i.e., capitalized, followed by a comma, and preceded by a space) in a case-sensitive manner. The replacement should only occur for the first occurrence of "Hello" at the beginning of a sentence. Do not use any built-in string manipulation functions or regular expressions.
"""

def replace_hello(string):
    result = ""
    sentences = string.split(".")
    
    for sentence in sentences:
        if sentence.startswith("Hello"):
            modified_sentence = "Goodbye" + sentence[len("Hello"):]
            result += modified_sentence
        else:
            result += sentence
        result += "."
    
    return result.rstrip(".")  # Remove the trailing period