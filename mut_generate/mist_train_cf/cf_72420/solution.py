"""
QUESTION:
Create a function named `get_alphanumeric_chars` that takes a string as input, extracts only alphanumeric characters, and replaces every third alphanumeric character with its corresponding ASCII value. The index of characters should be considered as one-based for determining every third character.
"""

def get_alphanumeric_chars(sentence):
    out_str = ''
    for i in range(len(sentence)):
        if sentence[i].isalnum():
            if ((i+1)%3 == 0):
                out_str += str(ord(sentence[i]))
            else:
                out_str += sentence[i]
    return out_str