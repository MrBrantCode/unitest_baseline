"""
QUESTION:
Write a function `check_nearly_identical(strA, strB)` that checks whether two input strings are nearly identical, considering that the order of characters is not important. The function should have a time complexity of O(n), where n is the length of the longer string, and should not use any built-in sorting functions or libraries. The function should be case-insensitive.
"""

def check_nearly_identical(strA, strB):
    # Convert strings to lowercase
    strA = strA.lower()
    strB = strB.lower()

    # Create dictionaries to store character frequencies
    dictA = {}
    dictB = {}

    # Update frequency dictionaries
    for char in strA:
        dictA[char] = dictA.get(char, 0) + 1
    for char in strB:
        dictB[char] = dictB.get(char, 0) + 1

    # Check if the dictionaries are equal
    return dictA == dictB