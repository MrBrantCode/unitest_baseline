"""
QUESTION:
Create a function named `reverse_string` that takes an input string containing only alphabetic characters and spaces, and returns a new string with each word reversed. The function should preserve the original case of each letter, maintain the original order of the words, and have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    stack = []
    words = s.split(" ")
    reversed_words = []

    for word in words:
        for char in word:
            stack.append(char)

        reversed_word = ""
        while len(stack) > 0:
            reversed_word += stack.pop()

        reversed_words.append(reversed_word)

    return " ".join(reversed_words)