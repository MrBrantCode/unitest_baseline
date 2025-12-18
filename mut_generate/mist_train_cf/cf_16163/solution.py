"""
QUESTION:
Write a Python function `reverse_sentence` that takes a sentence as input, reverses the order of the words, and reverses the letters within each word. The function should handle cases with multiple spaces between words, leading or trailing spaces, and special characters, numbers, or symbols in the sentence without using any built-in functions or libraries that directly solve the problem.
"""

def reverse_sentence(sentence):
    words = sentence.split(" ")
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = " ".join(reversed_words[::-1])
    return reversed_sentence