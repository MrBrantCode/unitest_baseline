"""
QUESTION:
Write a function `processDictionary` that takes a dictionary as input. The dictionary keys and values are strings of the form "key<number>" and "value<number>" respectively, where <number> is a positive integer. The function should return a tuple containing three values: the total count of entries in the dictionary, the sum of all key numbers extracted from the keys, and the sum of all value numbers extracted from the values.
"""

def processDictionary(dictionary):
    totalCount = 0
    sumKeyNumbers = 0
    sumValueNumbers = 0

    for key, value in dictionary.items():
        totalCount += 1

        # Extract keyNumber from a string of the form key<keyNumber>
        keyNumber = int(key[3:])

        # Extract valueNumber from a string of the form value<valueNumber>
        valueNumber = int(value[5:])

        sumKeyNumbers += keyNumber
        sumValueNumbers += valueNumber

    return totalCount, sumKeyNumbers, sumValueNumbers