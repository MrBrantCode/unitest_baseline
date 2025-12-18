"""
QUESTION:
Write a recursive function `countDistinctChars(text)` that calculates the total number of distinct characters in the input string `text`, excluding any whitespace characters. The function should also return the list of distinct characters in the order of their first occurrence. The input string may contain uppercase and lowercase letters, numbers, special characters, and punctuation marks.
"""

def countDistinctCharsRecursive(text, charSet, distinctChars):
    if len(text) == 0:
        return len(charSet), distinctChars
    if text[0].isspace():
        return countDistinctCharsRecursive(text[1:], charSet, distinctChars)
    if text[0] not in charSet:
        charSet.add(text[0])
        distinctChars.append(text[0])
    return countDistinctCharsRecursive(text[1:], charSet, distinctChars)

def countDistinctChars(text):
    charSet = set()
    distinctChars = []
    return countDistinctCharsRecursive(text, charSet, distinctChars)