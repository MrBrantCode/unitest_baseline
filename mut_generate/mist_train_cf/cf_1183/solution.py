"""
QUESTION:
Create a function named `reverse_sentence` that takes a string `sentence` as input. The function should reverse the order of the words in the sentence and also reverse the letters within each word. The function should handle cases with multiple spaces between words, leading or trailing spaces, special characters, and numbers. It should not use any built-in functions or libraries that directly solve the problem.
"""

def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse the order of the words and reverse the letters within each word
    reversed_words = [word[::-1] for word in words[::-1]]

    # Join the reversed words to form the reversed sentence
    reversed_sentence = " ".join(reversed_words)

    return reversed_sentence