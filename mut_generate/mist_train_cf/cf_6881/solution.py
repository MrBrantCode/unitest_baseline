"""
QUESTION:
Write a function `checkSameCharacters(stringA, stringB)` that checks if two strings have the same characters, frequency of characters, and are case sensitive. The function should also consider whitespace characters and punctuation marks. The function should have a time complexity of O(n), where n is the total length of the strings, and should not use any additional data structures or libraries other than an array of fixed size.
"""

def checkSameCharacters(stringA, stringB):
    frequency_array = [0] * 128

    for char in stringA:
        frequency_array[ord(char)] += 1

    for char in stringB:
        frequency_array[ord(char)] -= 1

    for count in frequency_array:
        if count != 0:
            return False

    return True