"""
QUESTION:
Find all unique pairs of numbers in an array that sum up to a given target integer. 

The array may contain duplicate elements, but the output should not contain duplicate pairs. Implement a function `findPairs(arr, target)` where `arr` is the array of integers and `target` is the target integer. The function should return a list of tuples, where each tuple contains a pair of numbers that sum up to the target. The function should have a time complexity of O(n) or better.
"""

def entrance(arr, target):
    result = set()
    numSet = set()
    
    for num in arr:
        diff = target - num
        if diff in numSet:
            pair = (min(num, diff), max(num, diff))
            result.add(pair)
        numSet.add(num)
    
    return list(result)