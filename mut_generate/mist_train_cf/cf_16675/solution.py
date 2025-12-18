"""
QUESTION:
Create a function `print_word_lengths` that accepts a string as input. The function should print each word in the string along with its character count, ignoring any special characters, numbers, and non-word characters. It should also handle strings with leading or trailing spaces. The function must be implemented using a recursive approach. The solution should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def print_word_lengths(string):
    # remove leading and trailing spaces
    string = string.strip()

    # base case: if the string is empty, return
    if not string:
        return

    # find the index of the first non-alphabetic character
    i = 0
    while i < len(string) and not string[i].isalpha():
        i += 1

    # find the index of the first space after the non-alphabetic character
    j = i
    while j < len(string) and string[j] != ' ':
        j += 1

    # extract the word and print its length
    word = string[i:j]
    print(word + ": " + str(len(word)))

    # recursively call the function with the remaining substring
    print_word_lengths(string[j:])