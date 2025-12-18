"""
QUESTION:
Create a function called `contains_all_letters` that determines if a given string contains all lowercase and uppercase letters of the English alphabet. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def contains_all_letters(string):
    alphabet = [False] * 52

    for char in string:
        if char.islower():
            index = ord(char) - ord('a')
            alphabet[index] = True
        elif char.isupper():
            index = ord(char) - ord('A') + 26
            alphabet[index] = True

    return all(alphabet)