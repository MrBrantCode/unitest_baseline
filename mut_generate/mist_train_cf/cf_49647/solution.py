"""
QUESTION:
Write a function `quantifyCharacterTotal` that takes a string as input and returns a tuple containing two values: the total count of characters in the string (including punctuation and spaces) and a dictionary where the keys are unique characters in the string and the values are their frequencies.
"""

def quantifyCharacterTotal(submittedString):
    characterCount = len(submittedString)
    frequencyDict = {}
    for char in submittedString:
        if char in frequencyDict:
            frequencyDict[char] += 1
        else:
            frequencyDict[char] = 1
    return characterCount, frequencyDict