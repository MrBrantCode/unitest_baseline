"""
QUESTION:
Implement a function `search_word(string, word)` that finds the position of a given word within a string without using any built-in string search or matching functions. The function should return the starting index of the word in the string, or -1 if the word is not found. The time complexity of the function should be O(n), where n is the length of the string, and the space complexity should be O(1).
"""

def search_word(string, word):
    # Check if the word is longer than the string
    if len(word) > len(string):
        return -1

    # Iterate through the string characters
    for i in range(len(string)):
        # Check if the current character matches the first character of the word
        if string[i] == word[0]:
            match = True
            # Iterate through the word characters and check if they match the corresponding string characters
            for j in range(len(word)):
                if i + j >= len(string) or string[i + j] != word[j]:
                    match = False
                    break
            # If all characters match, return the position of the word in the string
            if match:
                return i

    # If the word is not found, return -1
    return -1