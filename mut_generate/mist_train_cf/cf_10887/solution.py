"""
QUESTION:
Create a function `reverse_words` that takes a string of lowercase and uppercase letters, spaces, and punctuation marks as input. The function should return a string where the order of the words is reversed, while maintaining the capitalization of the first letter of each word. The function should handle multiple consecutive spaces and trailing spaces in the input string.
"""

def reverse_words(string):
    string = string.strip()
    words = string.split()
    words.reverse()
    for i in range(len(words)):
        words[i] = words[i][0].capitalize() + words[i][1:]
    reversed_string = ' '.join(words)
    return reversed_string