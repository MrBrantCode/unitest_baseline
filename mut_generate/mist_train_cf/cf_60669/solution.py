"""
QUESTION:
Write a function called `ReverseWordsInString` that takes an input string and returns a string with the words in reverse order. The function must preserve the original punctuation and case of the input string. The input string contains words separated by spaces.
"""

def ReverseWordsInString(input_string):
    words = input_string.split(' ')
    reversed_string = ' '.join(words[::-1])
    return reversed_string