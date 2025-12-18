"""
QUESTION:
Write a function `findLongestListKey(tagDict)` that takes a dictionary `tagDict` as input, where the keys are strings and the values are lists of strings. The function should return the key with the longest list as its value. If the dictionary is empty, the function should return `None`.
"""

def findLongestListKey(tagDict):
    maxTag = None
    for k, v in tagDict.items():
        if maxTag:
            if maxTag[1] < len(v):
                maxTag = (k, len(v))
        else:
            maxTag = (k, len(v))
    return None if maxTag is None else maxTag[0]