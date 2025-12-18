"""
QUESTION:
Write a function named `reverse_words` that takes a string as input and returns a new string with the words reversed, while maintaining the original order of punctuation marks and special characters. The function should only reverse alphabetic words and not alter the position or order of any non-alphabetic characters. The implementation should have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_words(string):
    word = ""
    result = ""
    for char in string:
        if char.isalpha():
            word += char
        else:
            if word:
                result += word[::-1] + char
                word = ""
            else:
                result += char
    if word:
        result += word[::-1]
    return result