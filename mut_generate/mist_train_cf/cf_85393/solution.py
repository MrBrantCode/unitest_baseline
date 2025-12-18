"""
QUESTION:
Write a function `isUniqueChars2` that determines if a string contains only unique characters using an additional data structure. The function should take a string as input and return a boolean value indicating whether the string contains only unique characters. Analyze the time and space complexity of your function. Provide a clear explanation of your reasoning. The input string is assumed to contain only ASCII characters.
"""

def isUniqueChars2(str):
    checker = [False]*128
    for char in str:
        val = ord(char)
        if checker[val]:
            return False
        checker[val] = True
    return True