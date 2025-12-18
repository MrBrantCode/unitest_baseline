"""
QUESTION:
Reverse the words in a given string without using in-built functions in Python. The function should have a time complexity of O(n) and a space complexity of O(1), and should reverse the entire string and then each word separately. 

The function should be named `reverse_words` and it should take a string `s` as an argument and return the string with its words reversed.
"""

def reverse_words(s):
    char_array = list(s)
    start = 0
    end = len(char_array) - 1
    while start < end:
        char_array[start], char_array[end] = char_array[end], char_array[start]
        start += 1
        end -= 1
    
    start = 0
    for i in range(len(char_array)):
        if char_array[i] == ' ':
            _reverse_word(char_array, start, i - 1)
            start = i + 1
    
    _reverse_word(char_array, start, len(char_array) - 1)
    
    reversed_string = ''.join(char_array)
    return reversed_string


def _reverse_word(char_array, start, end):
    while start < end:
        char_array[start], char_array[end] = char_array[end], char_array[start]
        start += 1
        end -= 1