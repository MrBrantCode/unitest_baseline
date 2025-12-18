"""
QUESTION:
Implement a function `get_uppercase_words` that takes a string of words as input and returns a list of uppercase words in the order of their appearance in the original string. The input string contains alphabetic characters and spaces, and its length is between 1 and 10^5. The function should have a time complexity of O(n) and should not use any built-in string parsing functions.
"""

def get_uppercase_words(string: str) -> list[str]:
    words = []
    word = ""
    for char in string:
        if char == " ":
            if word != "":
                words.append(word)
                word = ""
        elif char.isupper():
            word += char
    if word != "":
        words.append(word)
    return words