"""
QUESTION:
Create a function called `concatenate_words` that takes a string as input. The function should remove all spaces and special characters from the string, convert it to lowercase, and sort the resulting characters in alphabetical order.
"""

def concatenate_words(string):
    string = string.replace(" ", "")
    string = string.lower()
    string = ''.join(e for e in string if e.isalnum())
    string = ''.join(sorted(string))
    return string