"""
QUESTION:
Create a function called `getRange` that takes two integer parameters `minimum` and `maximum` and returns a list of integers between `minimum` and `maximum` (inclusive). The function should be able to handle both positive and negative numbers.
"""

def getRange(minimum, maximum):
    if minimum < maximum:
        return list(range(minimum, maximum + 1))
    else:
        return list(range(minimum, maximum - 1, -1))