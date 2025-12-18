"""
QUESTION:
Write a function `divide_and_convert` that takes a string as input. The function should split the input string into an array of individual words, ignoring any non-alphabetic characters and converting alternating words to uppercase and lowercase.
"""

def divide_and_convert(s):
    # Replace any numbers or special characters with whitespace
    s = ''.join(e for e in s if e.isalpha() or e.isspace())

    # Split the string into an array of individual lexical terms
    words = s.split()

    # Convert alternating terms to uppercase and lowercase
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].upper()
        else:
            words[i] = words[i].lower()

    return words