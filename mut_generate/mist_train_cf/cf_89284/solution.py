"""
QUESTION:
Implement a function `reverse_words(input_string)` that takes a string of words as input, ignores duplicate words, reverses each word in-place, removes non-alphabetic characters, and maintains the original order of words. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def reverse_words(input_string):
    result = []
    word = ""

    for char in input_string:
        if char.isalpha():
            word += char
        elif word:
            result.append(word[::-1])
            word = ""
            result.append(char)
        else:
            result.append(char)

    if word:
        result.append(word[::-1])

    return "".join(result)