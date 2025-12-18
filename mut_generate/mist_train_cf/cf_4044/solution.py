"""
QUESTION:
Implement a function `reverse_string` that takes a string of alphabetic characters (both uppercase and lowercase) with multiple words separated by spaces. The function should reverse each word individually while maintaining the original order of the words, and preserve the original case of each letter. The implementation should have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(string):
    stack = []
    words = string.split(" ")
    reversed_words = []

    for word in words:
        for char in word:
            stack.append(char)

        reversed_word = ""
        while len(stack) > 0:
            reversed_word += stack.pop()

        reversed_words.append(reversed_word)

    return " ".join(reversed_words)