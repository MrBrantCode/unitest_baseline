"""
QUESTION:
Given a function `twoSum(array, targetSum)`, determine if there are two distinct elements from the array that add up to the target sum. The function takes in an array of integers and a target sum, and returns a boolean indicating whether two such distinct elements exist. The array may contain negative numbers and will always have at least two elements. The solution should have a time complexity of O(n), where n is the length of the input array, and should optimize space complexity as much as possible without using built-in sorting functions or data structures.
"""

def twoSum(array, targetSum):
    numSet = set()
    for num in array:
        complement = targetSum - num
        if complement in numSet:
            return True
        numSet.add(num)
    return False