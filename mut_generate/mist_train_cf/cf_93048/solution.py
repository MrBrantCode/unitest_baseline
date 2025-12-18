"""
QUESTION:
Write a function `delete_every_third_character` that takes a string as input and returns a new string with every third character deleted, excluding the first character. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def delete_every_third_character(string):
    chars = list(string)
    writeIndex = 0
    readIndex = 0

    while readIndex < len(chars):
        if (readIndex + 1) % 3 != 0:
            chars[writeIndex] = chars[readIndex]
            writeIndex += 1
        readIndex += 1
    
    return ''.join(chars[:writeIndex])