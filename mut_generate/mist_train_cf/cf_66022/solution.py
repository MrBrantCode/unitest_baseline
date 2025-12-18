"""
QUESTION:
Construct a Python function named `capitalize_string` that takes a string as input, capitalizes the first letter of every word, and returns the modified string. The function should handle punctuation and multiple spaces between words correctly.
"""

def capitalize_string(input_string):
    words = input_string.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    result_string = ' '.join(capitalized_words)
    return result_string