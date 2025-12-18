"""
QUESTION:
Write a function `fetch_enclosed_alphabets(text)` that retrieves the first alphabet going from the end of the input string which is surrounded strictly by numerical digits. Ignore alphabets at the beginning or the end of the string. If such an alphabet does not exist, return an empty string. The input string consists only of alphanumeric characters.
"""

def fetch_enclosed_alphabets(text):
    """
    Pass in a string, then retrieve the first alphabet going from the end of the string which is surrounded strictly by numerical digits. Ignore alphabets at the beginning or the end of the string. If such an alphabet does not exist, return an empty string. Assume that the input string consists only of alphanumeric characters.
    """
    
    for i in reversed(range(1, len(text) - 1)):
        if text[i].isalpha() and text[i-1].isdigit() and text[i+1].isdigit():
            return text[i]

    return ""