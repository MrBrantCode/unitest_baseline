"""
QUESTION:
Write a function `getRange(minimum, maximum)` that returns all integers between `minimum` and `maximum` inclusive. The function should work with both positive and negative numbers.
"""

def getRange(minimum, maximum):
    if minimum < 0 and maximum < 0:
        return list(range(minimum, maximum + 1))
    elif minimum < 0 and maximum >= 0:
        return list(range(minimum, 0)) + list(range(0, maximum + 1))
    else:
        return list(range(minimum, maximum + 1))