"""
QUESTION:
Write a function `compressString` that takes a single string parameter `inputString` of length between 1 and 10^4, consisting only of lowercase English letters. The function should compress the string by replacing consecutive identical characters with a single instance of the character followed by the number of times it appears consecutively, and return the compressed string if it is shorter than the original string; otherwise, return the original string.
"""

def compressString(inputString):
    compressed = ""
    count = 1
    for i in range(1, len(inputString)):
        if inputString[i] == inputString[i - 1]:
            count += 1
        else:
            compressed += inputString[i - 1] + str(count)
            count = 1
    compressed += inputString[-1] + str(count)
    return inputString if len(compressed) >= len(inputString) else compressed