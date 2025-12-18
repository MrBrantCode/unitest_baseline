"""
QUESTION:
Write a function `remove_duplicates(sentence)` that takes a string of alphanumeric characters and spaces as input and returns a new string with all duplicate words removed, preserving the order of the remaining words. The function should be case-insensitive and ignore leading and trailing spaces. It should have a time complexity of O(n), where n is the length of the sentence, and should not use any built-in functions, additional data structures, nested loops, recursion, or external libraries.
"""

def remove_duplicates(sentence):
    unique_sentence = ""
    current_word = ""
    previous_word = ""
    index = 0

    while index < len(sentence):
        char = sentence[index]

        if char == " ":
            if current_word.lower() != previous_word.lower():
                unique_sentence += current_word + " "
                previous_word = current_word
            current_word = ""
        else:
            current_word += char

        index += 1

    if current_word.lower() != previous_word.lower():
        unique_sentence += current_word

    return unique_sentence