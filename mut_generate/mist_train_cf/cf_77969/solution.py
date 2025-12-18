"""
QUESTION:
Create a function `crop_string_to_length` that takes a string `str` and an integer `length` as parameters. The function should return the string `str` cropped to fit the given `length` while preserving words. If a word is longer than the given `length`, it should be omitted from the result. The cropped string should not end with a space.
"""

def crop_string_to_length(str, length):
    words = str.split()

    if length >= len(str):
        return str
    
    croppedString = ""
    currentLength = 0
    for word in words:
        wordLength = len(word)
        if currentLength + wordLength + 1 > length:
            break
        else:
            croppedString += word + ' '
            currentLength += wordLength + 1
            
    if croppedString.endswith(' '):
        croppedString = croppedString[:-1]

    return croppedString