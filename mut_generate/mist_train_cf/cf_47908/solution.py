"""
QUESTION:
Given a nested list of integers, write a function `depthSumInverse` that returns the sum of each integer in the list, with each integer being multiplied by its respective weight. The weight of an integer is calculated as `maxDepth - (the depth of the integer) + 1`, where `maxDepth` is the maximum depth of any integer in the list. The length of the nested list is between 1 and 50, the integers in the list range from -100 to 100, and the maximum depth of any integer is 50 or less.
"""

def depthSumInverse(nestedList):
    # Find maximum depth
    maxDepth = getMaxDepth(nestedList)
    # Calculate the weighted sum
    return getWeightedSum(nestedList, maxDepth)

def getMaxDepth(lst, depth = 1):
    maxDepth = depth
    for item in lst:
        if type(item) is list:
            maxDepth = max(maxDepth, getMaxDepth(item, depth + 1))
    return maxDepth

def getWeightedSum(lst, maxDepth, depth = 1):
    total = 0
    for item in lst:
        if type(item) is list:
            total += getWeightedSum(item, maxDepth, depth + 1)
        else:
            total += item * (maxDepth - depth + 1)
    return total