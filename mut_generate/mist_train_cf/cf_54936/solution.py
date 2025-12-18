"""
QUESTION:
Develop a function named 'sequence_identifier' that identifies a sequence of characters commencing with the letter 'a' and concluding with the letter 'b'. The function should handle incorrect inputs, including empty strings and strings that lack the letters 'a' or 'b', and yield a suitable error notification or return False in such cases.
"""

def sequence_identifier(input_string):
    if input_string == "":
        return "Empty input string received!"
    elif input_string[0] == 'a' and input_string[-1] == 'b':
        return True
    else:
        return False