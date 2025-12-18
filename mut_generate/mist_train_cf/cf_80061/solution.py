"""
QUESTION:
Write a function `reverse_second_words` that takes an input string, reverses every second word, and keeps the rest of the words in their original form. The input string can contain multiple words separated by spaces. The function should return the modified string.
"""

def reverse_second_words(input_string):
    words = input_string.split()
    for i in range(1, len(words), 2):
        words[i] = words[i][::-1]
    return ' '.join(words)