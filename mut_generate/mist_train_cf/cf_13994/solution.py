"""
QUESTION:
Delete every third character in a given string with a time complexity of O(n) and a space complexity of O(1). The function name should be "delete_every_third_character" and it should take a string as input. The function should modify the input string in-place and return the modified string.
"""

def delete_every_third_character(s):
    chars = list(s)
    writeIndex = 0
    readIndex = 0
    
    while readIndex < len(chars):
        if (readIndex + 1) % 3 != 0:
            chars[writeIndex] = chars[readIndex]
            writeIndex += 1
        readIndex += 1
    
    chars[writeIndex:] = []
    
    return ''.join(chars)