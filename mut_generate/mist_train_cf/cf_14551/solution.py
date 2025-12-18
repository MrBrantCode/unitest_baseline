"""
QUESTION:
Write a function `compressString` that takes a string as input and returns a compressed string where consecutive duplicate characters are removed and replaced with the character and the number of times it appears consecutively. The input string contains only uppercase and lowercase letters and can be up to 10^6 characters long. The function should have a time complexity of O(n) where n is the length of the input string.
"""

def compressString(inputString):
    """
    This function compresses a given string by replacing consecutive duplicate characters
    with the character and the number of times it appears consecutively.
    
    Args:
    inputString (str): The input string to be compressed.
    
    Returns:
    str: The compressed string.
    """
    if not inputString:
        return ""

    compressedString = ""
    count = 1
    previousChar = inputString[0]

    for i in range(1, len(inputString)):
        if inputString[i] == previousChar:
            count += 1
        else:
            compressedString += previousChar + str(count)
            count = 1
            previousChar = inputString[i]

    compressedString += previousChar + str(count)
    return compressedString