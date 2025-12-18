"""
QUESTION:
Write a function called `count_unique_characters` that takes a string as input and returns the number of unique characters in the string. The function should not use any additional data structures (e.g., sets, dictionaries, lists, etc.) or built-in string or array manipulation functions, and it should have a time complexity of O(n).
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