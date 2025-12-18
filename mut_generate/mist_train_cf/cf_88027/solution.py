"""
QUESTION:
Write a function `reverse_sentence(sentence)` that reverses a given sentence in Python without using built-in string reverse functions, methods, additional data structures, or string manipulation methods. The function should have a time complexity of O(n), where n is the length of the sentence, and should not use recursion or external libraries. The function should handle leading and trailing spaces, multiple spaces between words, and punctuation marks correctly, and should not modify the input sentence.
"""

def reverse_sentence(sentence):
    # Remove leading and trailing spaces
    sentence = sentence.strip()

    # Initialize variables
    reversed_sentence = ""
    word = ""

    # Iterate through the sentence in reverse order
    for i in range(len(sentence)-1, -1, -1):
        if sentence[i] != " ":
            # Add the current character to the word
            word = sentence[i] + word
        else:
            # Add the word to the reversed sentence
            reversed_sentence += word + " "
            word = ""

    # Add the last word to the reversed sentence
    reversed_sentence += word

    return reversed_sentence