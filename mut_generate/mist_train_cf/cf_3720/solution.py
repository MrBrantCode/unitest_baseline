"""
QUESTION:
Write a function named `count_unique_characters` that takes a string as input and returns the number of unique characters in the string. The function should not use any built-in string or array manipulation functions and should have a time complexity of O(n).
"""

def count_unique_characters(string):
    count = 0
    uniqueChars = ""
    duplicateChars = ""

    for char in string:
        if char in uniqueChars:
            if char in duplicateChars:
                continue
            else:
                duplicateChars += char
        else:
            count += 1
            uniqueChars += char

    return count