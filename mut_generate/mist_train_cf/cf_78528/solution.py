"""
QUESTION:
Create a function named `uniqueDictsByKey` that takes two parameters: a list of dictionaries `inputList` and a string `key`. The function should return a list of dictionaries where the values for the specified `key` are unique. If there are duplicate values for the specified `key`, only the first occurrence should be included in the output list.
"""

def uniqueDictsByKey(inputList, key):
    keySet = set()
    outputList = []

    for d in inputList:
        val = d[key]
        if val not in keySet:
            keySet.add(val)
            outputList.append(d)

    return outputList