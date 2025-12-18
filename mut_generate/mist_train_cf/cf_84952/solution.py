"""
QUESTION:
Build an Array With Stack Operations

Create a function `buildArray` that takes in a strictly increasing array `target` and an integer `n`. Return the sequence of operations ("Push" and "Pop") required to build the `target` array and the minimum number of operations. The operations are applied by reading numbers from the list `[1, 2, ..., n]`.
"""

def buildArray(target, n):
    result = [] 
    counter = 0 
    k = 1 
    for i in range(len(target)): 
        while k < target[i]: 
            result.append("Push")
            result.append("Pop")
            counter += 2
            k += 1
        result.append("Push")
        counter += 1
        k += 1
    return result, counter