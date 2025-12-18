"""
QUESTION:
Develop a function `removeExtraSpace` that takes one parameter `inputString` and returns the string with all leading, trailing, and extra spaces between words removed, leaving only single spaces between words.
"""

def removeExtraSpace(inputString):
    return ' '.join([word for word in inputString.split() if word != ''])